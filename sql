-- MySQL Script generated by MySQL Workbench
-- Mon Jun 12 19:28:17 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `project` ;

-- -----------------------------------------------------
-- Table `project`.`doanhthungay`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`doanhthungay` (
  `STT` INT NOT NULL AUTO_INCREMENT,
  `MaHoaDon` VARCHAR(255) NOT NULL,
  `ThuNgan` VARCHAR(255) NOT NULL,
  `TongHoaDon` INT NOT NULL,
  `KhachTra` INT NOT NULL,
  `Gio` TIME NOT NULL,
  `TenKhach` VARCHAR(45) NULL DEFAULT NULL,
  `Ngay` DATE NOT NULL,
  `Thang` VARCHAR(45) NOT NULL,
  `Donvingay` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`STT`),
  UNIQUE INDEX `STT_UNIQUE` (`STT` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project`.`giohang`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`giohang` (
  `STT` INT NOT NULL AUTO_INCREMENT,
  `Hoadon` VARCHAR(45) NOT NULL,
  `Tensanpham` VARCHAR(45) NOT NULL,
  `Masanpham` VARCHAR(45) NOT NULL,
  `Soluong` INT NOT NULL,
  `Tong` INT NOT NULL,
  `Loai` VARCHAR(45) NOT NULL,
  `Thuonghieu` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`STT`),
  UNIQUE INDEX `STT_UNIQUE` (`STT` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project`.`giohangluutru`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`giohangluutru` (
  `STT` INT NOT NULL AUTO_INCREMENT,
  `Hoadon` VARCHAR(45) NOT NULL,
  `Tensanpham` VARCHAR(45) NOT NULL,
  `Masanpham` VARCHAR(45) NOT NULL,
  `Soluong` INT NOT NULL,
  `Tong` INT NOT NULL,
  `Loai` VARCHAR(45) NOT NULL,
  `Thuonghieu` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`STT`),
  UNIQUE INDEX `STT_UNIQUE` (`STT` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project`.`khohang`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`khohang` (
  `STT` INT NOT NULL AUTO_INCREMENT,
  `Tensanpham` VARCHAR(255) NOT NULL,
  `Masanpham` VARCHAR(255) NOT NULL,
  `Thuonghieu` VARCHAR(255) NOT NULL,
  `Loai` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`STT`),
  UNIQUE INDEX `idkhohang_UNIQUE` (`STT` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 47
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project`.`sanpham`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`sanpham` (
  `STT` INT NOT NULL AUTO_INCREMENT,
  `Tensanpham` VARCHAR(45) NOT NULL,
  `Masanpham` VARCHAR(45) NOT NULL,
  `Soluong` VARCHAR(45) NOT NULL,
  `Dongia` INT NOT NULL,
  `Thuonghieu` VARCHAR(45) NOT NULL,
  `Loai` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`STT`),
  UNIQUE INDEX `idsanpham_UNIQUE` (`STT` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `project`.`taikhoan`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project`.`taikhoan` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Fullname` VARCHAR(45) NOT NULL,
  `Gioitinh` VARCHAR(45) NULL DEFAULT NULL,
  `Dantoc` VARCHAR(45) NULL DEFAULT NULL,
  `Ngay` VARCHAR(45) NULL DEFAULT NULL,
  `Thang` VARCHAR(45) NULL DEFAULT NULL,
  `Nam` VARCHAR(45) NULL DEFAULT NULL,
  `Tongiao` VARCHAR(45) NULL DEFAULT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `SDT` VARCHAR(45) NOT NULL,
  `Chucvu` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Ngaynhanviec` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`ID`, `Fullname`, `Username`, `Password`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
