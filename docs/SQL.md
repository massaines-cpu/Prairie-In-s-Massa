# [Exercice SQL](index.md)

Objectif : Créer une base de données, sous forme de tableau avec MySQL

### Dans People : Définir les données People
```sql
CREATE TABLE People (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    PoB INT,
    nom TEXT,
    heigh FLOAT,
    date_of_birth DATE
);
INSERT INTO People (PoB, nom, heigh, date_of_birth)
VALUES (266, 'Jason Derulo', 1.55, '1923-09-27');
```

### Définir les données dans City
```sql
INSERT INTO City (nom, lat, lon)
VALUES ('Jason Derulo', 1.198, 4.987);
CREATE TABLE City (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nom TEXT,
    lat FLOAT,
    lon FLOAT
);
```
### Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-Ines-Massa/tree/initiale/SQL)
