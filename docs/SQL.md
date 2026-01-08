# [Exercice SQL](index.md)

Objectif : Créer une base de données, sous forme de tableau avec MySQL

### Définir les données dans People
```sql
CREATE TABLE People (
    ID INT AUTO_INCREMENT PRIMARY KEY, #identifiant unique de chaque pers
    PoB INT,   #place of birth
    nom TEXT,
    heigh FLOAT,
    date_of_birth DATE
);
I
CREATE TABLE City (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nom TEXT,
    lat FLOAT,
    lon FLOAT
);

FOREIGN KEY (PoB) REFERENCES City(ID) #pour poB lié à ID de city

INSERT INTO People (PoB, nom, heigh, date_of_birth)
VALUES (266, 'Jason Derulo', 1.55, '1923-09-27');

INSERT INTO City (nom, lat, lon) #d'abord la ville pour qu'elle ait un ID
VALUES ('Jason Derulo', 1.198, 4.987);

```
### Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-Ines-Massa/tree/initiale/SQL)
