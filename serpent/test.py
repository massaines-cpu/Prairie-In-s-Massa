import json
from pprint import pprint
from termcolor import colored

with open('people.json', 'r') as p:
    people = json.loads(p.read())

#Nombre de femmes

nb_femmes = []
for person in people:
    if person["gender"] == "Female":
        nb_femmes.append(person)
print(f"Nombre de femmes : {len(nb_femmes)}")

#Nombre de personnes qui cherchent un homme 
personnes_qui_cherchent_hommes = []
for person in people:
    recherche = person["looking_for"]
    if person["looking_for"] == "M":
        personnes_qui_cherchent_hommes.append(person)
print(f"Nombre de personnes qui cherchent un homme : {len(personnes_qui_cherchent_hommes)}")

#Nombre de personnes qui cherchent une femme 
personnes_qui_cherchent_femmes = []
for person in people:
    recherche = person["looking_for"]
    if person["looking_for"] == "F":
        personnes_qui_cherchent_femmes.append(person)
print(f"Nombre de personnes qui cherchent un homme : {len(personnes_qui_cherchent_femmes)}")

#Nombre de personnes qui gagnent plus de 2000$
personnes_riches = []
for person in people:
    income = float(person["income"].replace("$",""))
    if income > 2000:
        personnes_riches.append(person)
print(f"Nombre de personnes qui gagnent plus de 2000$ : {len(personnes_riches)}")

#Nombre de personnes qui aiment les Drama 
personnes_drama = []
for person in people:
    preference = person["pref_movie"]
    if preference == "Drama":
        personnes_drama.append(person)
print(f"Nombre de personnes qui aiment les Drama : {len(personnes_drama)}")

#NNombre de femmes qui aiment la science-fiction

femmes_scifi = []
for person in people:
    preference = person["pref_movie"]
    gender = person["gender"]
    if preference == "Drama" and gender == "Female":
        femmes_scifi.append(person)
print(f"Nombre de femmes qui aiment la science-fiction : {len(femmes_scifi)}")

#Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$
personnes_docu_riches = []
for person in people:
    preference = person["pref_movie"]
    income = float(person["income"].replace("$",""))
    if preference == "Documentary" and income > 1482:
        personnes_docu_riches.append(person)
print(f"Nombre de personnes qui aiment les documentaires et gagnent plus de 1482$ : {len(personnes_docu_riches)}")

#Liste des noms, prénoms, id et revenus des personnes qui gagnent plus de 4000$
liste_personnes_riches = []
for person in people:
    income = float(person["income"].replace("$",""))
    if income > 4000:
        infos = {
            "Nom": person["last_name"],
            "Prénom": person["first_name"],
            "ID": person["id"],
            "Revenu": income
            }
        liste_personnes_riches.append(infos)

print(f"Liste des personnes qui gagnent plus de 4000$ : ")
for person in liste_personnes_riches:
    print(f"{person['Prénom']} {person['Nom']} (ID: {person['ID']}) - Revenu: ${person['Revenu']}")

#Homme le plus riche (nom et ID)
homme_riche = people[0]
salaire_max = 0
for person in people:
    if person["gender"] == "Male":
        income = float(person["income"].replace("$", ""))
        if income > salaire_max:
            salaire_max = income
            homme_riche = person
print(
    "L'homme le plus riche est :",
    homme_riche["last_name"],
    ", ID :", homme_riche["id"],
    ", Revenu :", salaire_max, "$")