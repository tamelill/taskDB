CREATE DATABASE  IF NOT EXISTS `project_scheme` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `project_scheme`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project_scheme
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `projects_table`
--

DROP TABLE IF EXISTS `projects_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects_table` (
  `idprojects_table` int(11) NOT NULL AUTO_INCREMENT,
  `Person` varchar(45) DEFAULT NULL,
  `Title` varchar(45) DEFAULT NULL,
  `Start` date DEFAULT NULL,
  `End` date DEFAULT NULL,
  `Done` tinyint(4) DEFAULT '0',
  `Description` text,
  PRIMARY KEY (`idprojects_table`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_table`
--

LOCK TABLES `projects_table` WRITE;
/*!40000 ALTER TABLE `projects_table` DISABLE KEYS */;
INSERT INTO `projects_table` VALUES (8,'Klaus','Klaus Serien','2017-04-01',NULL,0,'Lösungen machen + ergänzen'),(9,'Marc','Testate to Ilias','2016-12-01',NULL,1,'Testate to Ilias MAPH1'),(10,'Urs','Assessment Auswertung','2016-11-01',NULL,1,'Berufsschulen-Termin Urs Statistik'),(11,'Mirko','Serien PM erstellen','2017-01-01',NULL,0,'Serien translation De En, erstellen und lösen'),(12,'Urs','En-Assessments','2016-12-01',NULL,0,'Automatisierung,Excel Makro, Prozessoptimierung'),(13,'Tom','MAPH Testate Tom','2017-01-01',NULL,1,'Auswertung Testate'),(14,'Tom','Testate to Ilias MAPH2','2017-04-01',NULL,0,'Alte Prüfungsaufgaben nach ILIAS'),(15,'Marc','Nanotec to ILIAS','2016-11-15',NULL,1,'move to ilias '),(16,'Mirko','R evaluation','2016-12-01',NULL,1,'Rshiny, Rformat etc...'),(17,'Philipp','MAPH1Bau Testate Ilias','2017-04-01',NULL,0,'move to Ilias'),(18,'Mirko','Skript','2017-01-01',NULL,0,'Skripte versuchen zusammenzuführen'),(19,'Crabs','Crabs','2017-04-26',NULL,0,'Was du fentsch dä iitrag ned!');
/*!40000 ALTER TABLE `projects_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-26  9:11:41
