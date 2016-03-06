# -*- coding: utf-8 -*-

"""
  Wikipedia Hashtags
  ~~~~~~~~~~~~~~~~~~

  Some scripts for hashtags in Wikipedia edit comments.
"""

import os
import oursql
from collections import namedtuple

HT_DB_HOST = 's1.labsdb'  # enwiki db replica
HT_DB_NAME = 's52467__hashtags'

DB_CONFIG_PATH = os.path.expanduser('~/replica.my.cnf')  # Available by default on Labs

_rc_columns = ['rc_id',
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


RecentChangesModel = namedtuple('RC', _rc_columns)
HashtagRecentChangesModel = namedtuple('HTRC', ['htrc_id', 'htrc_lang'] + _rc_columns)


def db_connect(db, host, read_default_file=DB_CONFIG_PATH):
    connection = oursql.connect(db=db,
                                host=host,
                                read_default_file=read_default_file,
                                charset=None,
                                use_unicode=False)
    return connection


def ht_db_connect():
    return db_connect(HT_DB_NAME, HT_DB_HOST)
