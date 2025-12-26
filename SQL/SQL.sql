CREATE DATABASE Quinta;

USE Quinta;

CREATE TABLE People (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PoB INT,
    nom TEXT,
    heigh FLOAT,
    date_of_birth DATE
);

INSERT INTO People (PoB, nom, heigh, date_of_birth)
VALUES (266, 'Jason Derulo', 1.55, '1923-09-27');

CREATE TABLE City (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nom TEXT,
    lat FLOAT,
    lon FLOAT
);
INSERT INTO City (nom, lat, lon)
VALUES ('Jason Derulo', 1.198, 4.987);
