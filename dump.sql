-- MySQL dump 10.13  Distrib 8.0.33, for macos12.6 (arm64)
--
-- Host: localhost    Database: forum_project
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `forum_project`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `forum_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `forum_project`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add token',8,'add_tokenproxy'),(30,'Can change token',8,'change_tokenproxy'),(31,'Can delete token',8,'delete_tokenproxy'),(32,'Can view token',8,'view_tokenproxy'),(33,'Can add reply votes',9,'add_replyvotes'),(34,'Can change reply votes',9,'change_replyvotes'),(35,'Can delete reply votes',9,'delete_replyvotes'),(36,'Can view reply votes',9,'view_replyvotes'),(37,'Can add thread votes',10,'add_threadvotes'),(38,'Can change thread votes',10,'change_threadvotes'),(39,'Can delete thread votes',10,'delete_threadvotes'),(40,'Can view thread votes',10,'view_threadvotes'),(41,'Can add thread',11,'add_thread'),(42,'Can change thread',11,'change_thread'),(43,'Can delete thread',11,'delete_thread'),(44,'Can view thread',11,'view_thread'),(45,'Can add category',12,'add_category'),(46,'Can change category',12,'change_category'),(47,'Can delete category',12,'delete_category'),(48,'Can view category',12,'view_category'),(49,'Can add reply',13,'add_reply'),(50,'Can change reply',13,'change_reply'),(51,'Can delete reply',13,'delete_reply'),(52,'Can view reply',13,'view_reply');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$VSx1yilwRh0poqDtFSJH45$ysMq3Ln7LETZ3oggyC1xfy2XyIysi3dKQdVl7LQHDsg=','2023-06-28 22:04:29.490251',1,'testuser','','','test@us.er',1,1,'2023-06-23 18:08:05.094848'),(2,'pbkdf2_sha256$600000$GTTNJqwWKcIWwtUMu0thNg$OaoZEZIwFcnG1XdBVGiXqD2tzlmiOIZYmPsAQBE34zE=',NULL,0,'somefella','','','',0,1,'2023-06-23 19:31:46.538869'),(3,'pbkdf2_sha256$600000$I659OXCURTTW1piDTYfD17$cIkA77X7ngIjci7lPHMXAMRgWIl7TKC56J8f7lo+bHg=',NULL,0,'anotherfella','','','',0,1,'2023-06-23 20:49:14.626268');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('1c6d20057a08c0e357054a1c72f003facebe47b2','2023-06-23 20:49:23.182013',3),('3011ee7e1427b1ae6df622b92f2bc5d4473a783c','2023-06-23 18:35:39.839637',1),('37297745bdef2a73b1757aa7559c443760765bb7','2023-06-23 20:04:31.117246',2);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-06-23 18:14:21.895666','1','Category object (1)',1,'[{\"added\": {}}]',12,1),(2,'2023-06-23 18:14:29.097215','2','Category object (2)',1,'[{\"added\": {}}]',12,1),(3,'2023-06-23 18:14:51.734187','3','Category object (3)',1,'[{\"added\": {}}]',12,1),(4,'2023-06-23 18:35:39.840775','1','3011ee7e1427b1ae6df622b92f2bc5d4473a783c',1,'[{\"added\": {}}]',8,1),(5,'2023-06-23 19:31:46.680368','2','somefella',1,'[{\"added\": {}}]',4,1),(6,'2023-06-23 19:33:06.968279','1','Thread object (1)',1,'[{\"added\": {}}]',11,1),(7,'2023-06-23 19:36:34.433499','2','How to balance light reqs? - somefella',1,'[{\"added\": {}}]',11,1),(8,'2023-06-23 19:37:22.911489','3','Aquarium water for plants? - somefella',1,'[{\"added\": {}}]',11,1),(9,'2023-06-23 20:04:31.117848','2','37297745bdef2a73b1757aa7559c443760765bb7',1,'[{\"added\": {}}]',8,1),(10,'2023-06-23 20:49:14.764470','3','anotherfella',1,'[{\"added\": {}}]',4,1),(11,'2023-06-23 20:49:23.182832','3','1c6d20057a08c0e357054a1c72f003facebe47b2',1,'[{\"added\": {}}]',8,1),(12,'2023-06-23 21:08:22.811162','1','anotherfella - 2023-06-23 21:08:22.810053+00:00',1,'[{\"added\": {}}]',13,1),(13,'2023-06-23 21:09:01.499039','2','somefella - 2023-06-23 21:09:01.498193+00:00',1,'[{\"added\": {}}]',13,1),(14,'2023-06-23 21:09:28.111086','3','anotherfella - 2023-06-23 21:09:28.110038+00:00',1,'[{\"added\": {}}]',13,1),(15,'2023-06-23 22:06:50.854471','4','some title - anotherfella',3,'',11,1),(16,'2023-06-23 22:28:18.157611','1','ThreadVotes object (1)',1,'[{\"added\": {}}]',10,1),(17,'2023-06-23 22:28:26.839499','2','ThreadVotes object (2)',1,'[{\"added\": {}}]',10,1),(18,'2023-06-23 22:28:29.388579','1','ThreadVotes object (1)',2,'[]',10,1),(19,'2023-06-23 22:28:49.891744','1','ThreadVotes object (1)',2,'[{\"changed\": {\"fields\": [\"Upvote\"]}}]',10,1),(20,'2023-06-23 22:28:52.820903','2','ThreadVotes object (2)',2,'[{\"changed\": {\"fields\": [\"Upvote\"]}}]',10,1),(21,'2023-06-23 22:29:24.927332','1','ThreadVotes object (1)',2,'[]',10,1),(22,'2023-06-23 22:29:59.394177','1','ThreadVotes object (1)',2,'[]',10,1),(23,'2023-06-23 22:30:01.341210','2','ThreadVotes object (2)',2,'[]',10,1),(24,'2023-06-24 00:03:50.956061','4','ThreadVotes object (4)',3,'',10,1),(25,'2023-06-24 00:03:50.957868','3','ThreadVotes object (3)',3,'',10,1),(26,'2023-06-24 00:03:50.958920','2','ThreadVotes object (2)',3,'',10,1),(27,'2023-06-24 00:03:50.959878','1','ThreadVotes object (1)',3,'',10,1),(28,'2023-06-24 04:26:35.470093','6','ThreadVotes object (6)',3,'',10,1),(29,'2023-06-24 04:26:35.473296','5','ThreadVotes object (5)',3,'',10,1),(30,'2023-06-25 17:51:21.472514','5','a title - somefella',3,'',11,1),(31,'2023-06-25 22:30:35.467313','6','a title - somefella',3,'',11,1),(32,'2023-06-26 12:06:49.244504','1','ReplyVotes object (1)',1,'[{\"added\": {}}]',9,1),(33,'2023-06-26 12:06:58.263567','2','ReplyVotes object (2)',1,'[{\"added\": {}}]',9,1),(34,'2023-06-26 20:18:05.664820','5','ReplyVotes object (5)',3,'',9,1),(35,'2023-06-26 20:18:05.667355','4','ReplyVotes object (4)',3,'',9,1),(36,'2023-06-26 20:18:05.668341','3','ReplyVotes object (3)',3,'',9,1),(37,'2023-06-26 20:18:05.669139','2','ReplyVotes object (2)',3,'',9,1),(38,'2023-06-26 20:18:05.670346','1','ReplyVotes object (1)',3,'',9,1),(39,'2023-07-02 17:33:51.145838','2','somefella',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(40,'2023-07-02 17:34:04.616345','3','anotherfella',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1),(41,'2023-07-02 21:04:56.919993','4','somefella - 2023-07-02 21:04:56.917833+00:00',1,'[{\"added\": {}}]',13,1),(42,'2023-07-02 21:05:28.500441','7','Do I have too many plants??? - somefella',2,'[{\"changed\": {\"fields\": [\"Title\", \"Content\"]}}]',11,1),(43,'2023-07-02 21:06:04.586170','4','somefella - 2023-07-02 21:04:56.917833+00:00',2,'[{\"changed\": {\"fields\": [\"Content\"]}}]',13,1),(44,'2023-07-02 21:24:30.347780','6','ReplyVotes object (6)',1,'[{\"added\": {}}]',9,1),(45,'2023-07-02 21:24:41.792023','7','ReplyVotes object (7)',1,'[{\"added\": {}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(8,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(12,'forum','category'),(13,'forum','reply'),(9,'forum','replyvotes'),(11,'forum','thread'),(10,'forum','threadvotes'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-06-23 00:09:57.653741'),(2,'auth','0001_initial','2023-06-23 00:09:57.774180'),(3,'admin','0001_initial','2023-06-23 00:09:57.837416'),(4,'admin','0002_logentry_remove_auto_add','2023-06-23 00:09:57.840576'),(5,'admin','0003_logentry_add_action_flag_choices','2023-06-23 00:09:57.843300'),(6,'contenttypes','0002_remove_content_type_name','2023-06-23 00:09:57.949309'),(7,'auth','0002_alter_permission_name_max_length','2023-06-23 00:09:58.073530'),(8,'auth','0003_alter_user_email_max_length','2023-06-23 00:09:58.146980'),(9,'auth','0004_alter_user_username_opts','2023-06-23 00:09:58.190261'),(10,'auth','0005_alter_user_last_login_null','2023-06-23 00:09:58.224817'),(11,'auth','0006_require_contenttypes_0002','2023-06-23 00:09:58.227215'),(12,'auth','0007_alter_validators_add_error_messages','2023-06-23 00:09:58.234504'),(13,'auth','0008_alter_user_username_max_length','2023-06-23 00:09:58.264273'),(14,'auth','0009_alter_user_last_name_max_length','2023-06-23 00:09:58.287878'),(15,'auth','0010_alter_group_name_max_length','2023-06-23 00:09:58.301188'),(16,'auth','0011_update_proxy_permissions','2023-06-23 00:09:58.307431'),(17,'auth','0012_alter_user_first_name_max_length','2023-06-23 00:09:58.327621'),(18,'authtoken','0001_initial','2023-06-23 00:09:58.345548'),(19,'authtoken','0002_auto_20160226_1747','2023-06-23 00:09:58.354846'),(20,'authtoken','0003_tokenproxy','2023-06-23 00:09:58.355994'),(21,'sessions','0001_initial','2023-06-23 00:09:58.363150'),(22,'forum','0001_initial','2023-06-23 18:14:05.731426'),(23,'forum','0002_alter_replyvotes_reply_alter_replyvotes_user','2023-06-26 08:05:08.559131'),(24,'forum','0003_alter_replyvotes_reply_alter_replyvotes_user','2023-06-26 08:08:00.382464'),(26,'forum','0004_alter_replyvotes_upvote_alter_threadvotes_upvote','2023-06-26 11:15:59.260869');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('labujp4937gsnsb0jguzrah4d4e76q2e','.eJxVjEEOwiAQRe_C2hAIUgaX7j0DGWamUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVFWXX63TLSU-oO-IH13jS1usxT1ruiD9r1rbG8rof7d1Cwl60W6wwPHrfCC6AZQGzgkcDHYFxksM6JAWAcg0Q4ZwNIQplC8BGJ1ecL8b84ow:1qClCl:adkQW0WeI8XySQoQ7tQqS4jsUjDgFPwLetNsOZfy-p0','2023-07-07 18:08:19.592329'),('lwd7jnb2k8vk2m16ad2xcam83u0mgjli','.eJxVjEEOwiAQRe_C2hAIUgaX7j0DGWamUjWQlHZlvLtt0oVu_3vvv1XCdSlp7TKnidVFWXX63TLSU-oO-IH13jS1usxT1ruiD9r1rbG8rof7d1Cwl60W6wwPHrfCC6AZQGzgkcDHYFxksM6JAWAcg0Q4ZwNIQplC8BGJ1ecL8b84ow:1qG0xY:8JGRGNsSxttQOWi7lYbaak0IxRDEIzOJgPTvvIwPcXw','2023-07-16 17:34:04.621634');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_category`
--

DROP TABLE IF EXISTS `forum_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_category`
--

LOCK TABLES `forum_category` WRITE;
/*!40000 ALTER TABLE `forum_category` DISABLE KEYS */;
INSERT INTO `forum_category` VALUES (2,'Emergency!'),(1,'General Care'),(3,'Show-And-Tell');
/*!40000 ALTER TABLE `forum_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_reply`
--

DROP TABLE IF EXISTS `forum_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_reply` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_time_added` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `thread_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_reply_thread_id_cae3da2f_fk_forum_thread_id` (`thread_id`),
  KEY `forum_reply_user_id_73f8e234_fk_auth_user_id` (`user_id`),
  CONSTRAINT `forum_reply_thread_id_cae3da2f_fk_forum_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `forum_thread` (`id`),
  CONSTRAINT `forum_reply_user_id_73f8e234_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_reply`
--

LOCK TABLES `forum_reply` WRITE;
/*!40000 ALTER TABLE `forum_reply` DISABLE KEYS */;
INSERT INTO `forum_reply` VALUES (1,'2023-06-23 21:08:22.810053','Wish I knew fam. My plants are always roasting or suffocating.',2,3),(2,'2023-06-23 21:09:01.498193','Dangit. Sure would like to help these little friends',2,2),(3,'2023-06-23 21:09:28.110038','I figured it out. You have to do something called \'research\'...',2,3),(4,'2023-07-02 21:04:56.917833','Okay in my defense, I really really like plants',7,2);
/*!40000 ALTER TABLE `forum_reply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_replyvotes`
--

DROP TABLE IF EXISTS `forum_replyvotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_replyvotes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `upvote` tinyint(1) NOT NULL,
  `reply_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_replyvotes_reply_id_950e4b47_fk_forum_reply_id` (`reply_id`),
  KEY `forum_replyvotes_user_id_009db814_fk_auth_user_id` (`user_id`),
  CONSTRAINT `forum_replyvotes_reply_id_950e4b47_fk_forum_reply_id` FOREIGN KEY (`reply_id`) REFERENCES `forum_reply` (`id`),
  CONSTRAINT `forum_replyvotes_user_id_009db814_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_replyvotes`
--

LOCK TABLES `forum_replyvotes` WRITE;
/*!40000 ALTER TABLE `forum_replyvotes` DISABLE KEYS */;
INSERT INTO `forum_replyvotes` VALUES (6,1,4,3),(7,1,3,2);
/*!40000 ALTER TABLE `forum_replyvotes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_thread`
--

DROP TABLE IF EXISTS `forum_thread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_thread` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `date_time_added` datetime(6) NOT NULL,
  `locked` tinyint(1) NOT NULL,
  `content` longtext NOT NULL,
  `media_link` longtext NOT NULL,
  `category_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_thread_category_id_dcc73d52_fk_forum_category_id` (`category_id`),
  KEY `forum_thread_user_id_d501f243_fk_auth_user_id` (`user_id`),
  CONSTRAINT `forum_thread_category_id_dcc73d52_fk_forum_category_id` FOREIGN KEY (`category_id`) REFERENCES `forum_category` (`id`),
  CONSTRAINT `forum_thread_user_id_d501f243_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_thread`
--

LOCK TABLES `forum_thread` WRITE;
/*!40000 ALTER TABLE `forum_thread` DISABLE KEYS */;
INSERT INTO `forum_thread` VALUES (1,'How often should i water my succulents?','2023-06-23 19:33:06.967011',0,'I\'m worried I\'ve been overwatering my lil cacti guys but idk. Helppppppp','',1,2),(2,'How to balance light reqs?','2023-06-23 19:36:34.432308',0,'Trying to figure out how best to position my plants so they can receive optimal sunlight. Can anyone help me?','',1,2),(3,'Aquarium water for plants?','2023-06-23 19:37:22.910308',0,'Is waste water from my aquarium safe for my plants? Can provide detail about tank if needed. Freshwater.','',1,2),(7,'Do I have too many plants???','2023-06-28 04:15:00.426873',0,'Probably lols','',1,2);
/*!40000 ALTER TABLE `forum_thread` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forum_threadvotes`
--

DROP TABLE IF EXISTS `forum_threadvotes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `forum_threadvotes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `upvote` tinyint(1) NOT NULL,
  `thread_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `forum_threadvotes_thread_id_83ef9b8e_fk_forum_thread_id` (`thread_id`),
  KEY `forum_threadvotes_user_id_6b2b73fd_fk_auth_user_id` (`user_id`),
  CONSTRAINT `forum_threadvotes_thread_id_83ef9b8e_fk_forum_thread_id` FOREIGN KEY (`thread_id`) REFERENCES `forum_thread` (`id`),
  CONSTRAINT `forum_threadvotes_user_id_6b2b73fd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forum_threadvotes`
--

LOCK TABLES `forum_threadvotes` WRITE;
/*!40000 ALTER TABLE `forum_threadvotes` DISABLE KEYS */;
INSERT INTO `forum_threadvotes` VALUES (7,1,2,3),(8,1,2,2);
/*!40000 ALTER TABLE `forum_threadvotes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-02 14:32:38
