-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2020 at 05:42 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `retailbanking`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `Customer_ID` int(9) NOT NULL,
  `Account_ID` int(9) NOT NULL,
  `Account_Type` varchar(1) NOT NULL,
  `Balance` int(20) NOT NULL,
  `CR_date` varchar(9) DEFAULT NULL,
  `CR_last_date` varchar(9) DEFAULT NULL,
  `Duration` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`Customer_ID`, `Account_ID`, `Account_Type`, `Balance`, `CR_date`, `CR_last_date`, `Duration`) VALUES
(1, 1, 'S', 12500, '2020-06-1', '2020-06-1', 3),
(3, 2, 'S', 2495000, '2020-06-1', '2020-06-1', 3);

-- --------------------------------------------------------

--
-- Table structure for table `accountstatus`
--

CREATE TABLE `accountstatus` (
  `Customer_ID` int(9) NOT NULL,
  `Account_ID` int(9) NOT NULL,
  `Account_Type` text NOT NULL,
  `Status` text NOT NULL,
  `Message` text NOT NULL,
  `Last_Updated` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accountstatus`
--

INSERT INTO `accountstatus` (`Customer_ID`, `Account_ID`, `Account_Type`, `Status`, `Message`, `Last_Updated`) VALUES
(1, 1, 'S', 'Active', 'Account Successfully Created', '2020-06-18'),
(3, 2, 'S', 'Active', 'Account Successfully Created', '2020-06-18');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `SSN_ID` int(9) NOT NULL,
  `Customer_ID` int(9) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `City` varchar(20) NOT NULL,
  `State` varchar(20) NOT NULL,
  `Age` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`SSN_ID`, `Customer_ID`, `Name`, `Address`, `City`, `State`, `Age`) VALUES
(1, 1, 'Tiwari', 'Mandideep', 'Bhopal', 'MP', 22),
(2, 3, 'Arsalan', 'Phulwari Sharif', 'Patna', 'Bihar', 22);

-- --------------------------------------------------------

--
-- Table structure for table `customerstatus`
--

CREATE TABLE `customerstatus` (
  `SSN_ID` int(9) NOT NULL,
  `Customer_ID` int(9) NOT NULL,
  `Status` text NOT NULL,
  `Message` text NOT NULL,
  `Last_Updated` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customerstatus`
--

INSERT INTO `customerstatus` (`SSN_ID`, `Customer_ID`, `Status`, `Message`, `Last_Updated`) VALUES
(1, 1, 'Active', 'Customer Successfully Updated', '2020-06-18'),
(2, 2, 'Deactivated', 'Customer Deleted', '2020-06-18'),
(2, 3, 'Active', 'Customer Successfully Created', '2020-06-18');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `Source_Account_ID` int(9) NOT NULL,
  `Tgt_Account_ID` int(9) NOT NULL,
  `Amount` double NOT NULL,
  `Transaction_date` date NOT NULL,
  `Source_Acct_type` varchar(9) NOT NULL,
  `Target_Acct_type` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`Source_Account_ID`, `Tgt_Account_ID`, `Amount`, `Transaction_date`, `Source_Acct_type`, `Target_Acct_type`) VALUES
(2, 1, 5000, '2020-06-18', 'S', 'S');

-- --------------------------------------------------------

--
-- Table structure for table `userstore`
--

CREATE TABLE `userstore` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userstore`
--

INSERT INTO `userstore` (`username`, `password`) VALUES
('shubham', 'shubham@123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`Account_ID`),
  ADD UNIQUE KEY `Account_ID` (`Account_ID`);

--
-- Indexes for table `accountstatus`
--
ALTER TABLE `accountstatus`
  ADD PRIMARY KEY (`Customer_ID`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD UNIQUE KEY `Customer_ID` (`Customer_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `Account_ID` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `Customer_ID` int(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
