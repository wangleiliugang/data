-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: db3
-- ------------------------------------------------------
-- Server version	5.7.33-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CCB`
--

DROP TABLE IF EXISTS `CCB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CCB` (
  `name` varchar(20) DEFAULT NULL,
  `money` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CCB`
--

LOCK TABLES `CCB` WRITE;
/*!40000 ALTER TABLE `CCB` DISABLE KEYS */;
INSERT INTO `CCB` VALUES ('转钱',95000);
/*!40000 ALTER TABLE `CCB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ICBC`
--

DROP TABLE IF EXISTS `ICBC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ICBC` (
  `name` varchar(20) DEFAULT NULL,
  `money` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ICBC`
--

LOCK TABLES `ICBC` WRITE;
/*!40000 ALTER TABLE `ICBC` DISABLE KEYS */;
INSERT INTO `ICBC` VALUES ('借钱',7000);
/*!40000 ALTER TABLE `ICBC` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bjtab`
--

DROP TABLE IF EXISTS `bjtab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bjtab` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `bjtab_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `jfbab` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bjtab`
--

LOCK TABLES `bjtab` WRITE;
/*!40000 ALTER TABLE `bjtab` DISABLE KEYS */;
INSERT INTO `bjtab` VALUES (NULL,'小张',28000);
/*!40000 ALTER TABLE `bjtab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `c_name` varchar(15) DEFAULT NULL,
  `cfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,131100,'石家庄市',130000),(2,131101,'沧州市',130000),(3,131102,'廊坊市',130000),(4,131103,'西安市',140000),(5,131104,'成都市',150000),(6,131105,'重庆市',150000),(7,131106,'广州市',160000),(8,131107,'济南市',170000),(9,131108,'武汉市',180000),(10,131109,'郑州市',190000),(11,131110,'北京市',320000),(12,131111,'天津市',320000),(13,131112,'上海市',320000),(14,131113,'哈尔滨',320001),(15,131114,'雄安新区',320002);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jfbab`
--

DROP TABLE IF EXISTS `jfbab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jfbab` (
  `id` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `class` char(7) DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jfbab`
--

LOCK TABLES `jfbab` WRITE;
/*!40000 ALTER TABLE `jfbab` DISABLE KEYS */;
INSERT INTO `jfbab` VALUES (3,'小胡','AID1805',25000);
/*!40000 ALTER TABLE `jfbab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_t2`
--

DROP TABLE IF EXISTS `new_t2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `new_t2` (
  `id` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `likes` set('boy','girl','study') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_t2`
--

LOCK TABLES `new_t2` WRITE;
/*!40000 ALTER TABLE `new_t2` DISABLE KEYS */;
/*!40000 ALTER TABLE `new_t2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheng`
--

DROP TABLE IF EXISTS `sheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sheng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) DEFAULT NULL,
  `s_name` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheng`
--

LOCK TABLES `sheng` WRITE;
/*!40000 ALTER TABLE `sheng` DISABLE KEYS */;
INSERT INTO `sheng` VALUES (1,130000,'河北省'),(2,140000,'陕西省'),(3,150000,'四川省'),(4,160000,'广东省'),(5,170000,'山东省'),(6,180000,'湖北省'),(7,190000,'河南省'),(8,200000,'海南省'),(9,200001,'云南省'),(10,200002,'山西省'),(11,230000,'江苏省');
/*!40000 ALTER TABLE `sheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t1`
--

DROP TABLE IF EXISTS `t1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t1` (
  `id` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `likes` set('boy','girl','study') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t1`
--

LOCK TABLES `t1` WRITE;
/*!40000 ALTER TABLE `t1` DISABLE KEYS */;
/*!40000 ALTER TABLE `t1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t2`
--

DROP TABLE IF EXISTS `t2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t2` (
  `id` int(11) NOT NULL,
  `name` char(20) DEFAULT NULL,
  `likes` set('boy','girl','study') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t2`
--

LOCK TABLES `t2` WRITE;
/*!40000 ALTER TABLE `t2` DISABLE KEYS */;
/*!40000 ALTER TABLE `t2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t3`
--

DROP TABLE IF EXISTS `t3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(15) DEFAULT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t3`
--

LOCK TABLES `t3` WRITE;
/*!40000 ALTER TABLE `t3` DISABLE KEYS */;
INSERT INTO `t3` VALUES (12,'小王',26),(13,'小李',23),(14,'小张',25);
/*!40000 ALTER TABLE `t3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t888`
--

DROP TABLE IF EXISTS `t888`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t888` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t888`
--

LOCK TABLES `t888` WRITE;
/*!40000 ALTER TABLE `t888` DISABLE KEYS */;
INSERT INTO `t888` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `t888` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t999`
--

DROP TABLE IF EXISTS `t999`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t999` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t999`
--

LOCK TABLES `t999` WRITE;
/*!40000 ALTER TABLE `t999` DISABLE KEYS */;
/*!40000 ALTER TABLE `t999` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt1`
--

DROP TABLE IF EXISTS `tt1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tt1` (
  `username` char(20) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt1`
--

LOCK TABLES `tt1` WRITE;
/*!40000 ALTER TABLE `tt1` DISABLE KEYS */;
INSERT INTO `tt1` VALUES ('root',0,'/bin/bash'),('daemon',1,'/usr/sbin/nologin');
/*!40000 ALTER TABLE `tt1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tt2`
--

DROP TABLE IF EXISTS `tt2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tt2` (
  `username` char(20) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tt2`
--

LOCK TABLES `tt2` WRITE;
/*!40000 ALTER TABLE `tt2` DISABLE KEYS */;
INSERT INTO `tt2` VALUES ('root',0,0),('daemon',1,1),('bin',2,2);
/*!40000 ALTER TABLE `tt2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('daemon','x',1,1,'daemon','/usr/sbin','/usr/sbin/nologin'),('bin','x',2,2,'bin','/bin','/usr/sbin/nologin'),('sys','x',3,3,'sys','/dev','/usr/sbin/nologin'),('sync','x',4,65534,'sync','/bin','/bin/sync'),('games','x',5,60,'games','/usr/games','/usr/sbin/nologin'),('man','x',6,12,'man','/var/cache/man','/usr/sbin/nologin'),('lp','x',7,7,'lp','/var/spool/lpd','/usr/sbin/nologin'),('mail','x',8,8,'mail','/var/mail','/usr/sbin/nologin'),('news','x',9,9,'news','/var/spool/news','/usr/sbin/nologin'),('uucp','x',10,10,'uucp','/var/spool/uucp','/usr/sbin/nologin'),('proxy','x',13,13,'proxy','/bin','/usr/sbin/nologin'),('www-data','x',33,33,'www-data','/var/www','/usr/sbin/nologin'),('backup','x',34,34,'backup','/var/backups','/usr/sbin/nologin'),('list','x',38,38,'Mailing List Manager','/var/list','/usr/sbin/nologin'),('irc','x',39,39,'ircd','/var/run/ircd','/usr/sbin/nologin'),('gnats','x',41,41,'Gnats Bug-Reporting System (admin)','/var/lib/gnats','/usr/sbin/nologin'),('nobody','x',65534,65534,'nobody','/nonexistent','/usr/sbin/nologin'),('systemd-timesync','x',100,102,'systemd Time Synchronization,,,','/run/systemd','/bin/false'),('systemd-network','x',101,103,'systemd Network Management,,,','/run/systemd/netif','/bin/false'),('systemd-resolve','x',102,104,'systemd Resolver,,,','/run/systemd/resolve','/bin/false'),('systemd-bus-proxy','x',103,105,'systemd Bus Proxy,,,','/run/systemd','/bin/false'),('syslog','x',104,108,'','/home/syslog','/bin/false'),('_apt','x',105,65534,'','/nonexistent','/bin/false'),('messagebus','x',106,110,'','/var/run/dbus','/bin/false'),('uuidd','x',107,111,'','/run/uuidd','/bin/false'),('lightdm','x',108,114,'Light Display Manager','/var/lib/lightdm','/bin/false'),('whoopsie','x',109,116,'','/nonexistent','/bin/false'),('avahi-autoipd','x',110,119,'Avahi autoip daemon,,,','/var/lib/avahi-autoipd','/bin/false'),('avahi','x',111,120,'Avahi mDNS daemon,,,','/var/run/avahi-daemon','/bin/false'),('dnsmasq','x',112,65534,'dnsmasq,,,','/var/lib/misc','/bin/false'),('colord','x',113,123,'colord colour management daemon,,,','/var/lib/colord','/bin/false'),('speech-dispatcher','x',114,29,'Speech Dispatcher,,,','/var/run/speech-dispatcher','/bin/false'),('hplip','x',115,7,'HPLIP system user,,,','/var/run/hplip','/bin/false'),('kernoops','x',116,65534,'Kernel Oops Tracking Daemon,,,','/','/bin/false'),('pulse','x',117,124,'PulseAudio daemon,,,','/var/run/pulse','/bin/false'),('rtkit','x',118,126,'RealtimeKit,,,','/proc','/bin/false'),('saned','x',119,127,'','/var/lib/saned','/bin/false'),('usbmux','x',120,46,'usbmux daemon,,,','/var/lib/usbmux','/bin/false'),('tarena','x',1000,1000,'Yan Song','/home/tarena','/bin/bash'),('sshd','x',121,65534,'','/var/run/sshd','/usr/sbin/nologin'),('mysql','x',122,129,'MySQL Server,,,','/nonexistent','/bin/false'),('mongodb','x',123,65534,'','/var/lib/mongodb','/bin/false'),('redis','x',124,131,'','/var/lib/redis','/bin/false');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo2`
--

DROP TABLE IF EXISTS `userinfo2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo2` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo2`
--

LOCK TABLES `userinfo2` WRITE;
/*!40000 ALTER TABLE `userinfo2` DISABLE KEYS */;
INSERT INTO `userinfo2` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('daemon','x',1,1,'daemon','/usr/sbin','/usr/sbin/nologin'),('bin','x',2,2,'bin','/bin','/usr/sbin/nologin'),('sys','x',3,3,'sys','/dev','/usr/sbin/nologin'),('sync','x',4,65534,'sync','/bin','/bin/sync'),('games','x',5,60,'games','/usr/games','/usr/sbin/nologin'),('man','x',6,12,'man','/var/cache/man','/usr/sbin/nologin'),('lp','x',7,7,'lp','/var/spool/lpd','/usr/sbin/nologin'),('mail','x',8,8,'mail','/var/mail','/usr/sbin/nologin'),('news','x',9,9,'news','/var/spool/news','/usr/sbin/nologin'),('uucp','x',10,10,'uucp','/var/spool/uucp','/usr/sbin/nologin'),('proxy','x',13,13,'proxy','/bin','/usr/sbin/nologin'),('www-data','x',33,33,'www-data','/var/www','/usr/sbin/nologin'),('backup','x',34,34,'backup','/var/backups','/usr/sbin/nologin'),('list','x',38,38,'Mailing List Manager','/var/list','/usr/sbin/nologin'),('irc','x',39,39,'ircd','/var/run/ircd','/usr/sbin/nologin'),('gnats','x',41,41,'Gnats Bug-Reporting System (admin)','/var/lib/gnats','/usr/sbin/nologin'),('nobody','x',65534,65534,'nobody','/nonexistent','/usr/sbin/nologin'),('systemd-timesync','x',100,102,'systemd Time Synchronization,,,','/run/systemd','/bin/false'),('systemd-network','x',101,103,'systemd Network Management,,,','/run/systemd/netif','/bin/false'),('systemd-resolve','x',102,104,'systemd Resolver,,,','/run/systemd/resolve','/bin/false'),('systemd-bus-proxy','x',103,105,'systemd Bus Proxy,,,','/run/systemd','/bin/false'),('syslog','x',104,108,'','/home/syslog','/bin/false'),('_apt','x',105,65534,'','/nonexistent','/bin/false'),('messagebus','x',106,110,'','/var/run/dbus','/bin/false'),('uuidd','x',107,111,'','/run/uuidd','/bin/false'),('lightdm','x',108,114,'Light Display Manager','/var/lib/lightdm','/bin/false'),('whoopsie','x',109,116,'','/nonexistent','/bin/false'),('avahi-autoipd','x',110,119,'Avahi autoip daemon,,,','/var/lib/avahi-autoipd','/bin/false'),('avahi','x',111,120,'Avahi mDNS daemon,,,','/var/run/avahi-daemon','/bin/false'),('dnsmasq','x',112,65534,'dnsmasq,,,','/var/lib/misc','/bin/false'),('colord','x',113,123,'colord colour management daemon,,,','/var/lib/colord','/bin/false'),('speech-dispatcher','x',114,29,'Speech Dispatcher,,,','/var/run/speech-dispatcher','/bin/false'),('hplip','x',115,7,'HPLIP system user,,,','/var/run/hplip','/bin/false'),('kernoops','x',116,65534,'Kernel Oops Tracking Daemon,,,','/','/bin/false'),('pulse','x',117,124,'PulseAudio daemon,,,','/var/run/pulse','/bin/false'),('rtkit','x',118,126,'RealtimeKit,,,','/proc','/bin/false'),('saned','x',119,127,'','/var/lib/saned','/bin/false'),('usbmux','x',120,46,'usbmux daemon,,,','/var/lib/usbmux','/bin/false'),('tarena','x',1000,1000,'Yan Song','/home/tarena','/bin/bash'),('sshd','x',121,65534,'','/var/run/sshd','/usr/sbin/nologin'),('mysql','x',122,129,'MySQL Server,,,','/nonexistent','/bin/false'),('mongodb','x',123,65534,'','/var/lib/mongodb','/bin/false'),('redis','x',124,131,'','/var/lib/redis','/bin/false');
/*!40000 ALTER TABLE `userinfo2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo3`
--

DROP TABLE IF EXISTS `userinfo3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo3` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `comment` varchar(50) DEFAULT NULL,
  `homedir` varchar(50) DEFAULT NULL,
  `shell` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo3`
--

LOCK TABLES `userinfo3` WRITE;
/*!40000 ALTER TABLE `userinfo3` DISABLE KEYS */;
INSERT INTO `userinfo3` VALUES ('root','x',0,0,'root','/root','/bin/bash'),('daemon','x',1,1,'daemon','/usr/sbin','/usr/sbin/nologin'),('bin','x',2,2,'bin','/bin','/usr/sbin/nologin'),('sys','x',3,3,'sys','/dev','/usr/sbin/nologin'),('sync','x',4,65534,'sync','/bin','/bin/sync'),('games','x',5,60,'games','/usr/games','/usr/sbin/nologin'),('man','x',6,12,'man','/var/cache/man','/usr/sbin/nologin'),('lp','x',7,7,'lp','/var/spool/lpd','/usr/sbin/nologin'),('mail','x',8,8,'mail','/var/mail','/usr/sbin/nologin'),('news','x',9,9,'news','/var/spool/news','/usr/sbin/nologin');
/*!40000 ALTER TABLE `userinfo3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo4`
--

DROP TABLE IF EXISTS `userinfo4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo4` (
  `username` char(20) DEFAULT NULL,
  `password` char(1) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo4`
--

LOCK TABLES `userinfo4` WRITE;
/*!40000 ALTER TABLE `userinfo4` DISABLE KEYS */;
INSERT INTO `userinfo4` VALUES ('daemon','x',1),('bin','x',2),('sys','x',3),('sync','x',4),('games','x',5),('man','x',6),('lp','x',7),('mail','x',8),('news','x',9);
/*!40000 ALTER TABLE `userinfo4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xian`
--

DROP TABLE IF EXISTS `xian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x_id` int(11) DEFAULT NULL,
  `x_name` varchar(15) DEFAULT NULL,
  `xfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xian`
--

LOCK TABLES `xian` WRITE;
/*!40000 ALTER TABLE `xian` DISABLE KEYS */;
INSERT INTO `xian` VALUES (1,132100,'正定县',131100),(2,132102,'浦东新区',131112),(3,132103,'武昌区',131108),(4,132104,'哈哈',131115),(5,132105,'安新县',131114),(6,132106,'容城县',131114),(7,132107,'雄县',131114),(8,132108,'嘎嘎',131115);
/*!40000 ALTER TABLE `xian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-06 12:17:01
