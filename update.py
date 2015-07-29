# -*- coding: utf-8 -*-
"""
  Wikipedia Hashtags
  ~~~~~~~~~~~~~~~~~~

  Some scripts for hashtags in Wikipedia edit comments.

"""

import oursql
from argparse import ArgumentParser

from utils import find_hashtags
from dal import (db_connect, ht_db_connect, RecentChangesModel)

DEFAULT_HOURS = 24
DEFAULT_LANG =  'en'

DEBUG = True


class RecentChangeUpdater(object):
    def __init__(self, lang=DEFAULT_LANG, debug=DEBUG):
        self.lang = lang
        self.debug = debug
        self.ht_id_map = {}
        self.htrc_id_map = {}
        self.stats = {'changes_added': 0, 'tags_added': 0}

    def connect(self):
        wiki_db_name = self.lang + 'wiki_p'
        wiki_db_host = self.lang + 'wiki.labsdb'
        self.wiki_connect = db_connect(wiki_db_name, wiki_db_host)
        self.ht_connect = ht_db_connect()

    def _wiki_execute(self, query, params, as_dict=False):
        if as_dict:
            wiki_cursor = self.wiki_connect.cursor(oursql.DictCursor)
        else:
            wiki_cursor = self.wiki_connect.cursor()
        try:
            wiki_cursor.execute(query, params)
        except Exception as e:
            import pdb; pdb.set_trace()
        if self.debug and wiki_cursor.rowcount > 0:
            print 'affected %s rows' % wiki_cursor.rowcount
        return wiki_cursor

    def _ht_execute(self, query, params, as_dict=False):
        if as_dict:
            ht_cursor = self.ht_connect.cursor(oursql.DictCursor)
        else:
            ht_cursor = self.ht_connect.cursor()
        try:
            ht_cursor.execute(query, params)
        except oursql.CollatedWarningsError as e:
            #import pdb;pdb.set_trace()
            pass
        except Exception as e:
            #import pdb; pdb.set_trace()
            raise
        if self.debug and ht_cursor.rowcount > 0:
            #print 'affected %s rows' % ht_cursor.rowcount
            pass
        return ht_cursor

    def update_recentchanges(self, hours=DEFAULT_HOURS):
        rc_query = '''
            SELECT *
            FROM recentchanges
            WHERE rc_type = 0
            AND rc_timestamp > DATE_SUB(UTC_TIMESTAMP(), INTERVAL ? HOUR)
            AND rc_comment REGEXP ?
            ORDER BY rc_id DESC'''
        rc_params = (hours, '(^| )#[[:alpha:]]{2}[[:alnum:]]*[[:>:]]')
        if self.debug:
            print 'Searching for hashtags in last %s hours...' % hours
        cursor = self._wiki_execute(rc_query, rc_params)
        changes = cursor.fetchall()
        for change in changes:
            change = RecentChangesModel(*change)
            hashtags = find_hashtags(change.rc_comment)
            hashtags = [hashtag.lower() for hashtag in hashtags]
            htrc_id = self.add_recentchange(change)
            self.htrc_id_map[htrc_id] = hashtags
            for hashtag in hashtags:
                self.add_hashtag(hashtag, change.rc_timestamp)
        self.stats['total_changes'] = len(changes)
        for htrc_id, hashtags in self.htrc_id_map.items():
            for hashtag in hashtags:
                ht_id = self.ht_id_map[hashtag]
                if not ht_id:
                    import pdb;pdb.set_trace()
                    raise Exception('Missing ht_id')
                query = '''
                    INSERT INTO hashtag_recentchanges
                    VALUES (?, ?)'''
                params = (ht_id, htrc_id)
                try:
                    cursor = self._ht_execute(query, params)
                except oursql.IntegrityError as error_code:
                    if error_code[0] == 1062:
                        # Skip duplicate rows
                        pass
                    else:
                        raise error_code
        self.stats['total_tags'] = len(set([h for hs in self.htrc_id_map.values() for h in hs]))
        if self.debug:
            print 'Results'
            print '======='
            print 'Tags: %s new (of %s)' % (self.stats['tags_added'], self.stats['total_tags'])
            print 'Changes: %s new (of %s)' % (self.stats['changes_added'], self.stats['total_changes'])
        return self.stats

    def add_recentchange(self, rc):
        query = '''
            SELECT htrc_id
            FROM recentchanges
            WHERE rc_id = ?
            AND htrc_lang = ?
            LIMIT 1'''
        params = (rc[0], self.lang)
        cursor = self._ht_execute(query, params)
        htrc_id = cursor.fetchall()
        if htrc_id:
            return htrc_id[0][0]
        query = '''
            INSERT INTO recentchanges
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        params = (None, self.lang) + rc
        cursor = self._ht_execute(query, params)
        self.stats['changes_added'] += 1
        return cursor.lastrowid

    def get_ht_id(self, hashtag):
        query = '''
            SELECT ht_id, ht_update_timestamp
            FROM hashtags
            WHERE ht_text = ?
            LIMIT 1'''
        params = (hashtag,)
        cursor = self._ht_execute(query, params)
        ht_res = cursor.fetchall()
        return ht_res

    def add_hashtag(self, hashtag, rc_timestamp):
        #if hashtag in self.ht_id_map:
        #    return self.ht_id_map[hashtag]
        ht_res = self.get_ht_id(hashtag)
        if ht_res:
            self.ht_id_map[hashtag] = ht_res[0][0]
            if ht_res[0][1] < rc_timestamp:
                query = '''
                    UPDATE hashtags
                    SET ht_update_timestamp = ?
                    WHERE ht_text = ?'''
                params = (rc_timestamp, hashtag)
                cursor = self._ht_execute(query, params)
                self.stats['tags_added'] += 1
            return self.ht_id_map[hashtag]
        query = '''
            INSERT INTO hashtags
            VALUES (?, ?, UTC_TIMESTAMP() + 0, ?)'''
        params = (None, hashtag, rc_timestamp)
        cursor = self._ht_execute(query, params)
        self.ht_id_map[hashtag] = cursor.lastrowid  # Why does this return None?
        if not self.ht_id_map.get(hashtag):
            ht_res = self.get_ht_id(hashtag)
            self.ht_id_map[hashtag] = ht_res[0][0]
        self.stats['tags_added'] += 1
        return self.ht_id_map[hashtag]


def get_argparser():
    desc = 'Update the database of hashtags'
    prs = ArgumentParser(description=desc)
    prs.add_argument('--lang', default=DEFAULT_LANG)
    prs.add_argument('--hours', default=DEFAULT_HOURS)
    prs.add_argument('--debug', default=DEBUG, action='store_true')
    return prs


def main():
    parser = get_argparser()
    args = parser.parse_args()
    rc = RecentChangeUpdater(lang=args.lang, debug=args.debug)
    rc.connect()
    rc.update_recentchanges(hours=args.hours)


if __name__ == '__main__':
    main()
