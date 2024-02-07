-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema c3db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema c3db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `c3db` DEFAULT CHARACTER SET utf8 ;
USE `c3db` ;

-- -----------------------------------------------------
-- Table `c3db`.`UTENTI`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `c3db`.`UTENTI` (
  `CODICE` VARCHAR(32) NOT NULL,
  `NOME` VARCHAR(45) NOT NULL,
  `COGNOME` VARCHAR(45) NOT NULL,
  `USERNAME` VARCHAR(45) NOT NULL,
  `PASSWORD` VARCHAR(45) NOT NULL,
  `ETA` INT NOT NULL,
  `SESSO` CHAR(1) NOT NULL,
  `CFISCALE` CHAR(16) NOT NULL,
  `NAZIONALITA` CHAR(3) NOT NULL,
  `INDIRIZZO` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`CODICE`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
