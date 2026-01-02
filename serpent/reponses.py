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
    if films == "Drama":
        drama_lover.append(person)
print(f"Nombre de personnes qui aiment les Drama : {len(drama_lover)}")

#Nombre de femmes qui aiment la science-fiction
femmes_lover = []
for person in people:
    if person["gender"] == "Female":
        films = person["pref_movie"].replace("|","")
        if films == "Sci-Fi":
            femmes_lover.append(person)
print(f"Nombre de femmes qui aiment la science-fiction : {len(femmes_lover)}")

#LEVEL 2
# Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$
docu_riche = []
for person in people:
    films = person["pref_movie"].replace("|","")
    income = float(person["income"].replace("$",""))
    if films == "Documentary" and income > 1482:
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