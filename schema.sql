-- Switch to the directory where this file is and login with PostgresSQL client
-- Import this file

/*
* CREATE DATABASE IF NOT IN PLACE
*/
CREATE DATABASE IF NOT EXISTS andelabootcamp;

-- Change to the database

\connect andelabootcamp

/*
* Relations
*/



-- Relation Users
CREATE TABLE IF NOT EXISTS users(
  uid serial PRIMARY KEY,
  firstname VARCHAR(50) not null,
  lastname VARCHAR(50) not null,
  email VARCHAR(100) not null unique,
  username VARCHAR(100) not null unique,
  password VARCHAR(128) not null
);

-- Relation Diary
CREATE TABLE IF NOT EXISTS diary(
  did serial PRIMARY KEY,
  username VARCHAR(100) not null,
  entry TEXT,
  event_date DATE,
  entry_date DATE,
  notification_date DATE,
  version VARCHAR(100),
  FOREIGN KEY username REFERENCES users(username) ON UPDATE CASCADE ON DELETE RESTRICT,
  FOREIGN KEY version REFERENCES apiversion(version) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS apiversion(
  vid serial PRIMARY KEY,
  version VARCHAR(100)
)

/*
* AUDIT TRAIL TABLE FOR DIARY - TO ADD TRIGGERS
*/

CREATE TABLE IF NOT EXISTS diary_audit_trail like diary;
