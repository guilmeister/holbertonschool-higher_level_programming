-- Comments:
-- Script that creates the database hbtn_0c_0 in your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT PRIMARY KEY UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL);