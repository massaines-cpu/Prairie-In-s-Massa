import json
from pprint import pprint
from termcolor import colored

with open('people.json', 'r') as p:
    people = json.loads(p.read())

#option 1 : calcul

femmes = 1000-491
print(f"Nombre de femmes : {femmes}")

#option 2
femmes2 = []                        # un tableau vide
for person in people:               # pour chaque persone du tableau
    if person["gender"] == "Female":  # si c'est un homme (2-266-02250-4)
        femmes2.append(person)      # je l'ajoute au tableau
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