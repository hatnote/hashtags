
-- begin run logs

CREATE TABLE start_log (start_log_id integer not null auto_increment,
                       start_timestamp TIMESTAMP,
                       lang varchar(8),
                       command varchar(1024),
                       run_uuid varchar(36),
                       PRIMARY KEY (start_log_id),
                       KEY (start_timestamp),
                       KEY (lang));

CREATE TABLE complete_log (complete_log_id integer not null auto_increment,
                           complete_timestamp TIMESTAMP,
                           lang varchar(8),
                           output varchar(4096),
                           run_uuid varchar(36),
                           PRIMARY KEY (complete_log_id),
                           KEY (complete_timestamp),
                           KEY (lang));

-- end run logs

CREATE TABLE /*_*/hashtags (
  ht_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  ht_text varbinary(767) NOT NULL default '',
  ht_create_timestamp varbinary(14) NOT NULL default '',
  ht_update_timestamp varbinary(14) NOT NULL default '');

CREATE INDEX /*i*/ht_text ON hashtags (ht_text);
CREATE INDEX /*i*/ht_create_timestamp ON hashtags (ht_create_timestamp);

CREATE TABLE /*_*/mentions (
  mn_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  mn_text varbinary(767) NOT NULL default '',
  mn_create_timestamp varbinary(14) NOT NULL default '',
  mn_update_timestamp varbinary(14) NOT NULL default '');

CREATE INDEX /*i*/mn_text ON mentions (mn_text);
CREATE INDEX /*i*/mn_create_timestamp ON mentions (mn_create_timestamp);

CREATE_TABLE /*_*/mention_recentchanges (
  mn_id int NOT NULL,
  mnrc_id int NOT NULL);

CREATE TABLE /*_*/hashtag_recentchanges (
  ht_id int NOT NULL,
  htrc_id int NOT NULL);

CREATE UNIQUE INDEX /*i*/htrc_hashtag_recentchanges ON /*_*/hashtag_recentchanges (ht_id, htrc_id);
CREATE INDEX /*i*/htrc_hashtag ON /*_*/hashtag_recentchanges (ht_id);

CREATE TABLE /*_*/recentchanges (
  htrc_id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  htrc_lang varchar(32) NOT NULL default '',
  rc_id int NOT NULL,
  rc_timestamp varbinary(14) NOT NULL default '',
  rc_cur_time varbinary(14) NOT NULL default '',

  -- As in revision
  rc_user int unsigned NOT NULL default 0,
  rc_user_text varchar(255) binary NOT NULL,

  -- When pages are renamed, their RC entries do _not_ change.
  rc_namespace int NOT NULL default 0,
  rc_title varchar(255) binary NOT NULL default '',

  -- as in revision...
  rc_comment varbinary(767) NOT NULL default '',
  rc_minor tinyint unsigned NOT NULL default 0,

  -- Edits by user accounts with the 'bot' rights key are
  -- marked with a 1 here, and will be hidden from the
  -- default view.
  rc_bot tinyint unsigned NOT NULL default 0,

  -- Set if this change corresponds to a page creation
  rc_new tinyint unsigned NOT NULL default 0,

  -- Key to page_id (was cur_id prior to 1.5).
  -- This will keep links working after moves while
  -- retaining the at-the-time name in the changes list.
  rc_cur_id int unsigned NOT NULL default 0,

  -- rev_id of the given revision
  rc_this_oldid int unsigned NOT NULL default 0,

  -- rev_id of the prior revision, for generating diff links.
  rc_last_oldid int unsigned NOT NULL default 0,

  -- The type of change entry (RC_EDIT,RC_NEW,RC_LOG,RC_EXTERNAL)
  rc_type tinyint unsigned NOT NULL default 0,

  -- The source of the change entry (replaces rc_type)
  -- default of '' is temporary, needed for initial migration
  rc_source varchar(16) binary not null default '',

  -- If the Recent Changes Patrol option is enabled,
  -- users may mark edits as having been reviewed to
  -- remove a warning flag on the RC list.
  -- A value of 1 indicates the page has been reviewed.
  rc_patrolled tinyint unsigned NOT NULL default 0,

  -- Recorded IP address the edit was made from, if the
  -- $wgPutIPinRC option is enabled.
  rc_ip varbinary(40),

  -- Text length in characters before
  -- and after the edit
  rc_old_len int,
  rc_new_len int,

  -- Visibility of recent changes items, bitfield
  rc_deleted tinyint unsigned NOT NULL default 0,

  -- Value corresponding to log_id, specific log entries
  rc_logid int unsigned NOT NULL default 0,
  -- Store log type info here, or null
  rc_log_type varbinary(255) NULL default NULL,
  -- Store log action or null
  rc_log_action varbinary(255) NULL default NULL,
  -- Log params
  rc_params blob NULL
);

CREATE INDEX /*i*/rc_timestamp ON /*_*/recentchanges (rc_timestamp);
CREATE INDEX /*i*/rc_lang_namespace_title ON /*_*/recentchanges (htrc_lang, rc_namespace, rc_title);
CREATE INDEX /*i*/rc_lang_cur_id ON /*_*/recentchanges (htrc_lang, rc_cur_id);
CREATE INDEX /*i*/lang_new_name_timestamp ON /*_*/recentchanges (htrc_lang, rc_new,rc_namespace,rc_timestamp);
CREATE INDEX /*i*/rc_ip ON /*_*/recentchanges (rc_ip);
CREATE INDEX /*i*/rc_lang_ns_usertext ON /*_*/recentchanges (htrc_lang, rc_namespace, rc_user_text);
CREATE INDEX /*i*/rc_lang_user_text ON /*_*/recentchanges (htrc_lang, rc_user_text, rc_timestamp);
