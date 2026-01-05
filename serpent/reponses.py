import json
from pprint import pprint
from termcolor import colored

with open('people.json', 'r') as p:
    people = json.loads(p.read())

#option 1 : calcul

femmes = 1000-491
print(f"Nombre de femmes : {femmes}")

#option 2
femmes2 = []                        
for person in people:               
    if person["gender"] == "Female":  
        femmes2.append(person)      
print(f"Nombre de femmes : {len(femmes2)}")

#nombre de personne qui cherche homme
charo = []
for person in people:
    if person["looking_for"] == "M":
        charo.append(person)
print(f"Nombre de personne qui cherchent un homme : {len(charo)}")

#nombre de personne qui cherche femme
charo2 = []
for person in people:
    if person["looking_for"] == "F":
        charo2.append(person)
print(f"Nombre de personne qui cherchent une femme : {len(charo2)}")

#Nombre de personnes qui gagnent plus de 2000$ 
riche = []
for person in people:
    argent = person["income"]
    argent_converti = float(argent.replace("$",""))
    if argent_converti > 2000:
        riche.append(person)
print(f"Nombre de personne qui gagne plus de 2000$ : {len(riche)}")

#Nombre de personnes qui aiment les Drama 
drama_lover = []
for person in people:
    films = person["pref_movie"].replace("|","")
    if "Drama" in films:
        drama_lover.append(person)
print(f"Nombre de personnes qui aiment les Drama : {len(drama_lover)}")

#Nombre de femmes qui aiment la science-fiction
femmes_lover = []
for person in people:
    if person["gender"] == "Female":
        films = person["pref_movie"].replace("|","")
        if "Sci-Fi" in films:
            femmes_lover.append(person)
print(f"Nombre de femmes qui aiment la science-fiction : {len(femmes_lover)}")

#LEVEL 2
# Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$
docu_riche = []
for person in people:
    films = person["pref_movie"].replace("|","")
    income = float(person["income"].replace("$",""))
    if "Documentary" in films and income > 1482:
        docu_riche.append(person)
print(f"Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$ : {len(docu_riche)}")

#Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$
personnes_riches = []
for person in people:
    income = float(person["income"].replace("$",""))
    if income > 4000:
        infos = {
            "nom": person["last_name"],
            "prenom": person["first_name"],
            "id": person["id"],
            "revenu": income
        }
        personnes_riches.append(infos)
#faut print toutes les personnes concernées par 4000
#if person["income"]>4000 print person["income"].[name].[prenom].[id]>4000
print(f"Liste des personnes qui gagnent plus de 4000$ : ")
for person in personnes_riches:
    print(f"{person["prenom"]} {person["nom"]} (ID: {person["id"]}) - Revenu: ${person["revenu"]}")
 
 #Homme le plus riche (nom et id)
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

#Salaire moyen
salaires = 0
for person in people:
    income = float(person["income"].replace("$",""))
    salaires = salaires + income
    salaire_moyen = salaires / len(people)

print(f"salaire moyen : {salaire_moyen}")
#la moyenne c'est tout les salaires additionnés divisé par le nombre de salaire

#Salaire médian 
# faut classer les salaires dans un ordre croissant
# si impair = (n+1) ÷ 2
# si pair = (n ÷ 2) + 1

salaires = []
for person in people:
    income = float(person["income"].replace("$",""))
    salaires.append(income)

salaires.sort()
nombre_salaires = len(salaires)
if nombre_salaires % 2 == 0:
    salaire_median = (salaires[nombre_salaires // 2 - 1] + salaires[nombre_salaires // 2]) / 2
else:
    salaire_median = salaires[nombre_salaires // 2]

print("Salaire médian :", salaire_median)

#Nombre de personnes qui habitent dans l'hémisphère nord 
#habiter dans l'hemisphere nord equivaut a avoir une latitude positive
#donc chercher dans people toutes les personnes avec une latitude positive

hemis_nord = 0
for person in people:
    latitude = float(person["latitude"])
    if latitude > 0:
        hemis_nord += 1
print(f"Nombre de personnes qui habitent dans l'hémisphère nord :", hemis_nord)

#autre technique
personnes_hemis_nord = []
for person in people:
    latitude = float(person["latitude"])
    if latitude > 0:
        personnes_hemis_nord.append(person)
print(f"Nombre de personnes qui habitent dans l'hémisphère nord : {len(personnes_hemis_nord)}")

#Salaire moyen des personnes qui habitent dans l'hémisphère sud 
#d'abord gerer hemisphere sud puis dans hemisphere le salaire
hemis_sud = 0
salaires = 0
for person in people:
    latitude = float(person["latitude"])
    if latitude < 0:
        hemis_sud += 1
        income = float(person["income"].replace("$",""))
        salaires += income

salaire_moyen = salaires / hemis_sud
print(f"Salaire moyen : {salaire_moyen}")

#autre technique

hemis_sud = []
salaires = 0
for person in people:
    latitude = float(person["latitude"])
    if latitude < 0:
        hemis_sud.append(person)
        income = float(person["income"].replace("$",""))
        salaires += income

salaire_moyen = salaires / len(hemis_sud)
print(f"Salaire moyen : {salaire_moyen}")

#Personne qui habite le plus près de Bérénice Cawt (nom et id)
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
#Les noms et ids des 23 personnes qui travaillent chez google
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

#personne la plus âgée
#y'a pas une bibliotheque pour les calendriers???
#faut lui dire que cest ce format la "annee"/"mois"/"jour"
#de le calculer 2026 - "date de naissance"
from datetime import datetime

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

#personne la plus jeune
#y'a pas une bibliotheque pour les calendriers???
#faut lui dire que cest ce format la "annee"/"mois"/"jour"
#de le calculer 2026 - "date de naissance"
from datetime import datetime

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

#Genre de film le plus populaire
list_genre_film = {}

for person in people:
    films = person["pref_movie"].replace("|", " ")
    genres = films.split()

    for genre in genres:
        if genre in list_genre_film:
            list_genre_film[genre] += 1
        else: 
            list_genre_film[genre] = 1

genre_gagnant = ""
genre_max = 0

for genre_nom in list_genre_film:
    genre_actuel = list_genre_film[genre_nom] 
    
    if genre_actuel > genre_max:
        genre_max = genre_actuel   
        genre_gagnant = genre_nom

print("le genre le plus populaire est :", genre_gagnant)

#Genres de film par ordre de popularité
list_genre_film_ordre = {genre: list_genre_film[genre] for genre in sorted(list_genre_film, key=list_genre_film.get)}

print("Liste dans l'ordre", list_genre_film_ordre)


#Liste des genres de film et nombre de personnes qui les préfèrent
list_genre_film2 = {}

for person in people:
    films = person["pref_movie"].replace("|", " ")
    genres = films.split()

    for genre in genres:
        if genre in list_genre_film2:
            list_genre_film2[genre] += 1
        else: 
            list_genre_film2[genre] = 1

print("Liste des genres de film et nombre de personnes qui les préfèrent :", list_genre_film2)

#Age moyen des hommes qui aiment les films noirs
from datetime import datetime

somme_age = 0
hommes_noirs = 0

for person in people:
    genre = person["gender"]
    films = person["pref_movie"]
    birthday = person["date_of_birth"]
    birthday_convert = datetime.strptime(birthday, "%Y-%m-%d")
    age = 2026 - date_naissance.year

    if genre == "Male" and "Film-Noir" in films:
        hommes_noirs += 1
        somme_age += age

age_moyen = somme_age / hommes_noirs

print(f"Age moyen des hommes qui aiment les films noirs est de {int(age_moyen)} ans ")
