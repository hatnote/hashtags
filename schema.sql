/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `complete_log` (
  `complete_log_id` int(11) NOT NULL AUTO_INCREMENT,
  `complete_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lang` varbinary(8) DEFAULT NULL,
  `output` varbinary(4096) DEFAULT NULL,
  `run_uuid` varbinary(36) DEFAULT NULL,
  PRIMARY KEY (`complete_log_id`),
  KEY `complete_timestamp` (`complete_timestamp`),
  KEY `lang` (`lang`)
) ENGINE=Aria AUTO_INCREMENT=1514514 DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hashtag_recentchanges` (
  `ht_id` int(11) NOT NULL,
  `htrc_id` int(11) NOT NULL,
  UNIQUE KEY `htrc_hashtag_recentchanges` (`ht_id`,`htrc_id`),
  KEY `htrc_hashtag` (`ht_id`)
) ENGINE=Aria DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hashtags` (
  `ht_id` int(11) NOT NULL AUTO_INCREMENT,
  `ht_text` varbinary(767) NOT NULL DEFAULT '',
  `ht_create_timestamp` varbinary(14) NOT NULL DEFAULT '',
  `ht_update_timestamp` varbinary(14) NOT NULL DEFAULT '',
  PRIMARY KEY (`ht_id`),
  KEY `ht_text` (`ht_text`),
  KEY `ht_create_timestamp` (`ht_create_timestamp`)
) ENGINE=Aria AUTO_INCREMENT=36146 DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mention_recentchanges` (
  `mn_id` int(11) NOT NULL,
  `mnrc_id` int(11) NOT NULL
) ENGINE=Aria DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mentions` (
  `mn_id` int(11) NOT NULL AUTO_INCREMENT,
  `mn_text` varbinary(767) NOT NULL DEFAULT '',
  `mn_create_timestamp` varbinary(14) NOT NULL DEFAULT '',
  `mn_update_timestamp` varbinary(14) NOT NULL DEFAULT '',
  PRIMARY KEY (`mn_id`),
  KEY `mn_text` (`mn_text`),
  KEY `mn_create_timestamp` (`mn_create_timestamp`)
) ENGINE=Aria AUTO_INCREMENT=129 DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recentchanges` (
  `htrc_id` int(11) NOT NULL AUTO_INCREMENT,
  `htrc_lang` varbinary(32) NOT NULL DEFAULT '',
  `rc_id` int(11) NOT NULL,
  `rc_timestamp` varbinary(14) NOT NULL DEFAULT '',
  `rc_cur_time` varbinary(14) NOT NULL DEFAULT '',
  `rc_user` int(10) unsigned NOT NULL DEFAULT '0',
  `rc_user_text` varbinary(255) NOT NULL,
  `rc_namespace` int(11) NOT NULL DEFAULT '0',
  `rc_title` varbinary(255) NOT NULL DEFAULT '',
  `rc_comment` varbinary(767) NOT NULL DEFAULT '',
  `rc_minor` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_bot` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_new` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_cur_id` int(10) unsigned NOT NULL DEFAULT '0',
  `rc_this_oldid` int(10) unsigned NOT NULL DEFAULT '0',
  `rc_last_oldid` int(10) unsigned NOT NULL DEFAULT '0',
  `rc_type` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_source` varbinary(16) NOT NULL DEFAULT '',
  `rc_patrolled` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_ip` varbinary(40) DEFAULT NULL,
  `rc_old_len` int(11) DEFAULT NULL,
  `rc_new_len` int(11) DEFAULT NULL,
  `rc_deleted` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `rc_logid` int(10) unsigned NOT NULL DEFAULT '0',
  `rc_log_type` varbinary(255) DEFAULT NULL,
  `rc_log_action` varbinary(255) DEFAULT NULL,
  `rc_params` blob,
  PRIMARY KEY (`htrc_id`),
  KEY `rc_timestamp` (`rc_timestamp`),
  KEY `rc_lang_namespace_title` (`htrc_lang`,`rc_namespace`,`rc_title`),
  KEY `rc_lang_cur_id` (`htrc_lang`,`rc_cur_id`),
  KEY `lang_new_name_timestamp` (`htrc_lang`,`rc_new`,`rc_namespace`,`rc_timestamp`),
  KEY `rc_ip` (`rc_ip`),
  KEY `rc_lang_ns_usertext` (`htrc_lang`,`rc_namespace`,`rc_user_text`),
  KEY `rc_lang_user_text` (`htrc_lang`,`rc_user_text`,`rc_timestamp`),
  KEY `rc_id_htrc_lang` (`rc_id`,`htrc_lang`) COMMENT 'speed up add_recentchange 20160305'
) ENGINE=Aria AUTO_INCREMENT=5566734 DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `start_log` (
  `start_log_id` int(11) NOT NULL AUTO_INCREMENT,
  `start_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lang` varbinary(8) DEFAULT NULL,
  `command` varbinary(1024) DEFAULT NULL,
  `run_uuid` varbinary(36) DEFAULT NULL,
  PRIMARY KEY (`start_log_id`),
  KEY `start_timestamp` (`start_timestamp`),
  KEY `lang` (`lang`)
) ENGINE=Aria AUTO_INCREMENT=1529298 DEFAULT CHARSET=binary PAGE_CHECKSUM=1;
/*!40101 SET character_set_client = @saved_cs_client */;
