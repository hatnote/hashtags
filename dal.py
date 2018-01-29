# -*- coding: utf-8 -*-

"""
  Wikipedia Hashtags
  ~~~~~~~~~~~~~~~~~~

  Some scripts for hashtags in Wikipedia edit comments.
"""

import os
import oursql
from collections import namedtuple

HT_DB_HOST = 'tools.db.svc.eqiad.wmflabs'
HT_DB_NAME = 's52467__new_hashtags'

# Tools can use two db services:
#   *.analytics.db.svc.eqiad.wmflabs (for big queries)
#   *.web.db.svc.eqiad.wmflabs (for quick queries)
WIKI_DB_DOMAIN = 'web.db.svc.eqiad.wmflabs'

DB_CONFIG_PATH = os.path.expanduser('~/replica.my.cnf')  # Available by default on Labs

RC_COLUMNS = ['rc_id',
              'rc_timestamp',
              'rc_user',
              'rc_user_text',
              'rc_namespace',
              'rc_title',
              'rc_comment',
              'rc_minor',
              'rc_bot',
              'rc_new',
              'rc_cur_id',
              'rc_this_oldid',
              'rc_last_oldid',
              'rc_type',
              'rc_source',
              'rc_patrolled',
              'rc_ip',
              'rc_old_len',
              'rc_new_len',
              'rc_deleted',
              'rc_logid',
              'rc_log_type',
              'rc_log_action',
              'rc_params']


RecentChangesModel = namedtuple('RC', RC_COLUMNS)
HashtagRecentChangesModel = namedtuple('HTRC', ['htrc_id', 'htrc_lang'] + RC_COLUMNS)


def db_connect(db, host, read_default_file=DB_CONFIG_PATH):
    connection = oursql.connect(db=db,
                                host=host,
                                read_default_file=read_default_file,
                                charset=None,
                                use_unicode=False)
    return connection

def wiki_db_connect(lang):
    wiki_db_name = lang + 'wiki_p'
    wiki_db_host = lang + 'wiki.' + WIKI_DB_DOMAIN
    return db_connect(wiki_db_name, wiki_db_host)


def ht_db_connect():
    return db_connect(HT_DB_NAME, HT_DB_HOST)
