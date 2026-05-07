Enter password: 
-- MySQL dump 10.13  Distrib 9.6.0, for Linux (x86_64)
--
-- Host: localhost    Database: mc_manager
-- ------------------------------------------------------
-- Server version	9.6.0

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
Warning: A partial dump from a server that has GTIDs will by default include the GTIDs of all transactions, even those that changed suppressed parts of the database. If you don't want to restore GTIDs, pass --set-gtid-purged=OFF. To make a complete dump, pass --all-databases --triggers --routines --events. 
Warning: A dump from a server that has GTIDs enabled will by default include the GTIDs of all transactions, even those that were executed during its extraction and might not be represented in the dumped data. This might result in an inconsistent data dump. 
In order to ensure a consistent backup of the database, pass --single-transaction or --lock-all-tables or --source-data. 
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a8b16fea-48b6-11f1-9a81-aa9f4f410b9c:1-34';

--
-- Dumping data for table `Bases`
--

LOCK TABLES `Bases` WRITE;
/*!40000 ALTER TABLE `Bases` DISABLE KEYS */;
INSERT INTO `Bases` VALUES (1,'Kuronagi Village',4,NULL),(2,'The Circus',3,1),(3,'EXSTO',7,2);
/*!40000 ALTER TABLE `Bases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Events`
--

LOCK TABLES `Events` WRITE;
/*!40000 ALTER TABLE `Events` DISABLE KEYS */;
INSERT INTO `Events` VALUES (1,7,'Bloodsport','A PvP Tournament hosted by The Crimson Guard','2026-04-04 18:00:00');
/*!40000 ALTER TABLE `Events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Faction_Memberships`
--

LOCK TABLES `Faction_Memberships` WRITE;
/*!40000 ALTER TABLE `Faction_Memberships` DISABLE KEYS */;
INSERT INTO `Faction_Memberships` VALUES (1,3,1),(2,5,1),(3,6,1),(4,7,2);
/*!40000 ALTER TABLE `Faction_Memberships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Factions`
--

LOCK TABLES `Factions` WRITE;
/*!40000 ALTER TABLE `Factions` DISABLE KEYS */;
INSERT INTO `Factions` VALUES (1,'The Rubber Mafia',3),(2,'The Crimson Guard',7);
/*!40000 ALTER TABLE `Factions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Players`
--

LOCK TABLES `Players` WRITE;
/*!40000 ALTER TABLE `Players` DISABLE KEYS */;
INSERT INTO `Players` VALUES (1,'DeathZamboni','Owning the server'),(2,'AnderAlfus','Head admin, basically runs the server himself'),(3,'Swift_AF','Managing the shopping district, head of the rubber mafia'),(4,'Banh_Bread','Being a cheerful, joyous, and generally likeable person'),(5,'Xelaqua','Fairly average minecraft player'),(6,'Easporks','Being blue'),(7,'Kuvahunter','Building a giant tower'),(8,'Kimm','Using a skin with a funny cat face, and convncing a lot of other people to do the same'),(9,'Scubawheel','Refusing to wear armor, opting for only a pair of copper boots'),(10,'Domkar1','the guy everyone hates on for no reason');
/*!40000 ALTER TABLE `Players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `Shops`
--

LOCK TABLES `Shops` WRITE;
/*!40000 ALTER TABLE `Shops` DISABLE KEYS */;
INSERT INTO `Shops` VALUES (1,9,'Scuba Storage','Containers, such as chests'),(2,8,'Firework Store','Fireworks');
/*!40000 ALTER TABLE `Shops` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-07  9:37:15
