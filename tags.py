# -*- coding: utf-8 -*-
"""
  Wikipedia Hashtags
  ~~~~~~~~~~~~~~~~~~

  Some scripts for hashtags in Wikipedia edit comments.

"""

import oursql
from argparse import ArgumentParser
from pprint import pprint

from dal import ht_db_connect


def get_all_tags():
    connection = ht_db_connect()
    cursor = connection.cursor()
    query = '''
    SELECT ht_text, ht_update_timestamp
    FROM hashtags'''
    cursor.execute(query)
    return cursor.fetchall()


def get_tagged_changes(tag):
    connection = ht_db_connect()
    cursor = connection.cursor(oursql.DictCursor)
    query = '''
    SELECT *
    FROM recentchanges AS rc
    JOIN hashtag_recentchanges AS htrc
      ON htrc.htrc_id = rc.htrc_id
    JOIN hashtags AS ht
      ON ht.ht_id = htrc.ht_id
    WHERE ht.ht_text = ?'''
    params = (tag,)
    cursor.execute(query, params)
    return cursor.fetchall()


def get_argparser():
    prs = ArgumentParser()
    prs.add_argument('--show', action='store_true')
    prs.add_argument('--tag', default=None)
    return prs


if __name__ == '__main__':
    parser = get_argparser()
    args = parser.parse_args()
    if args.show:
        tag_list = get_all_tags()
        pprint(tag_list)
    if args.tag:
        tagged_changes = get_tagged_changes(args.tag)
        pprint(tagged_changes)
