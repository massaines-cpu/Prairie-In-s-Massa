
# [Exerice Tinder](index.md)

Objectif : Écrire un code qui permet d’afficher la réponse à chacune de ces questions.

## Partie 1 : Analyse
il y a un code qui permet d'afficher les réponses, donc les réponses sont déjà presentes dans le document... il faut trouver un moyen de les récupérer et de les afficher.

Elles doivent être dans people.json. 
1. Comment les appeler
2. Comment les mettre sous forme de questions
3. Comment associer ces réponses à leurs questions respectives

## Partie 2 : Questions
- j'ai pris la même forme de boucle à chaque fois (à peu près) et je l'adapte

1. Pour nombre de femmes :
```python
print(colored("Nombre de femmes : ", 'yellow'))
femmes = [p for p in people if p['gender'] == 'Female']
pprint(len(femmes))
```
ou faire le nombre total de personnes - le nombre d'hommes
```python
femmes = 1000-491
print(f"Nombre de femmes : {femmes}")
```
2. Ce que les personnes cherchent
Donc on veut savoir le nombre de personnes qui cherche un "M" et le nombre de personne qui cherche un "F"

## Nombre de personnes qui cherchent homme
```python
charo = []
for person in people:
    if person["looking_for"] == "M":
        charo.append(person)
print(f"Nombre de personne qui cherchent un homme : {len(charo)}")
```
## Nombre de personnes qui cherchent femme
```python
charo2 = []
for person in people:
    if person["looking_for"] == "F":
        charo2.append(person)
print(f"Nombre de personne qui cherchent une femme : {len(charo2)}")
```
## Nombre de personnes qui gagnent plus de 2000$ 
```python
riche = []
for person in people:
    argent = person["income"]
    argent_converti = float(argent.replace("$",""))
    if argent_converti > 2000:
        riche.append(person)
print(f"Nombre de personne qui gagne plus de 2000$ : {len(riche)}")
```
## Nombre de personnes qui aiment les Drama 
```python
drama_lover = []
for person in people:
    films = person["pref_movie"]
    films_converti = films.replace("|","")
    if films == "Drama":
        drama_lover.append(person)
print(f"Nombre de personnes qui aiment les Drama : {len(drama_lover)}")
```
## Nombre de femmes qui aiment la science-fiction
```python
femmes_lover = []
for person in people:
    if person["gender"] == "Female":
        films = person["pref_movie"]
        films_converti = films.replace("|","")
        if films == "Sci-Fi":
            femmes_lover.append(person)
print(f"Nombre de femmes qui aiment la science-fiction : {len(femmes_lover)}")
```
### LEVEL 2
## Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$
```python
docu_riche = []
for person in people:
    films = person["pref_movie"].replace("|","")
    income = float(person["income"].replace("$",""))
    if films == "Documentary" and income > 1482:
        docu_riche.append(person)
print(f"Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$ : {len(docu_riche)}")
```
## Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$
```python
all_infos = []
for person in people:
    income = float(person["income"].replace("$",""))
    if income > 4000:
        infos = {
            "nom": person["last_name"],
            "prenom": person["first_name"],
            "id": person["id"],
            "revenu": income
        }
        `all_infos.append(infos)`
`#faut print toutes les personnes concernées par 4000`
`#if person["income"]>4000 print person["income"].[name].[prenom].[id]>4000`
`print("Liste des personnes qui gagnent plus de 4000$ :")`

for person in all_infos:
    print(
        "Nom :", person["nom"],
        ", Prénom :", person["prenom"],
        ", ID :", person["id"],
        ", Revenu :", person["revenu"], "$")
 ```
## Homme le plus riche (nom et id)
```python
homme_riche = people[0]
revenu_max = 0

for person in people:
    if person["gender"] == "Male":
        income = float(person["income"].replace("$",""))

        if income > revenu_max:
            revenu_max = income
            homme_riche = person

print(
    "L'homme le plus riche est :",
    homme_riche["last_name"],
    ", ID :", homme_riche["id"],
    ", Revenu :", revenu_max, "$")
```
## Salaire moyen
```python
salaires = 0
for person in people:
    income = float(person["income"].replace("$",""))
    salaires = salaires + income
    salaire_moyen = salaires / len(people)

print(f"salaire moyen : {salaire_moyen}")
#la moyenne c'est tout les salaires additionnés divisé par le nombre de salaires
```
## Personne qui habite le plus près de Bérénice Cawt (nom et id)
```python
#besoin de savoir les coordonnées de berenice ("latitude":15.5900396,"longitude":-87.879523)
#person["latitude","longitude"] < berenice["latitude", "longitude" < person["latitude", "longitude"]

berenice_lat = 15.5900396
berenice_long = -87.879523
voisine = people[0]
min_distance = abs(float(voisine["latitude"]) - berenice_lat) + abs(float(voisine["longitude"]) - berenice_long)

for person in people:
    if person["first_name"] == "Bérénice" and person["last_name"] == "Cawt":
            continue
    latitude = float(person["latitude"])
    longitude = float(person["longitude"])
    distance = abs(latitude - berenice_lat) + abs(longitude - berenice_long)
    
    if distance < min_distance:
        min_distance = distance
        voisine = person

print(
    "La personne la plus proche de Bérénice est :",
    voisine["first_name"], voisine["last_name"],
    "| ID :", voisine["id"]
)
```
## Les noms et ids des 23 personnes qui travaillent chez google
```python
google_lover = []
for person in people:
    email = person["email"]
    if "google" in email:
        infos = {
            "nom" : person["last_name"],
            "prenom" : person["first_name"],
            "id" : person["id"]
        }
        google_lover.append(infos)
print("Les noms et ids des 23 personnes qui travaillent chez google: ")
for person in google_lover:
    print(f"{person["prenom"]} {person["nom"]} (ID: {person["id"]})")
```
## Personne la plus âgée
```python
#y'a pas une bibliotheque pour les calendriers???
#faut lui dire que cest ce format la "annee"/"mois"/"jour"
#de le calculer 2026 - "date de naissance"

la_vieille = people[0]
age_max = -1 
for person in people:
    birthday = person["date_of_birth"]
    date_naissance = datetime.strptime(birthday, "%Y-%m-%d")
    age = 2026 - date_naissance.year
    
    if age > age_max:
        age_max = age
        la_vieille = person

print(f"La personne la plus âgée est {la_vieille['first_name']} {la_vieille['last_name']}.\nElle a {age_max} ans en 2026.")
```
## Personne la plus jeune

```python
la_jeune = people[0]
age_mini = 200
for person in people:
    birthday = person["date_of_birth"]
    date_naissance = datetime.strptime(birthday, "%Y-%m-%d")
    age = 2026 - date_naissance.year
    
    if age < age_mini:
        age_mini = age
        la_jeune = person

print(f"La personne la plus jeune est {la_jeune['first_name']} {la_jeune['last_name']}.\nElle a {age_mini} ans en 2026.")
```
Bon j'ai pas tout mis car tout est dispo sur le lien, je me suis arrêtée à "Age moyen des femmes qui aiment les drames et habitent sur le fuseau horaire, de Paris"
## Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-Ines-Massa/blob/initiale/serpent/reponses.py)
