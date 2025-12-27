
# EXERCICE PYTHON

Objectif : Vous devez écrire le code qui permet d’afficher la réponse à chacune de ces questions.

## Partie 1 : Analyse
il y a un code qui permet d'afficher les réponses, donc les réponses sont déjà presentes dans le document... il faut trouver un moyen de les récupérer et de les afficher.

Elles doivent être dans people.json. 
1. Comment les appeler
2. Comment les mettre sous forme de questions
3. Comment associer ces réponses à leurs questions respectives

## Partie 2 : Questions

1. Pour nombre de femmes :
`print(colored("Nombre de femmes : ", 'yellow'))`
`femmes = [p for p in people if p['gender'] == 'Female']`
`pprint(len(femmes))`

ou faire le nombre total de personnes - le nombre d'hommes
`femmes = 1000-491`
`print(f"Nombre de femmes : {femmes}")`

2. Ce que les personnes cherchent
Donc on veut savoir le nombre de personnes qui cherche un "M" et le nombre de personne qui cherche un "F"

#nombre de personnes qui cherchent homme
`charo = []`
`for person in people:`
    `if person["looking_for"] == "M":`
       ` charo.append(person)`
`print(f"Nombre de personne qui cherchent un homme : {len(charo)}")`

#nombre de personnes qui cherchent femme
`charo2 = []`
`for person in people:`
    `if person["looking_for"] == "F":`
        `charo2.append(person)`
`print(f"Nombre de personne qui cherchent une femme : {len(charo2)}")`

#nombre de personnes qui gagnent plus de 2000$ 
`riche = []`
`for person in people:`
    `argent = person["income"]`
    `argent_converti = float(argent.replace("$",""))`
    `if argent_converti > 2000:`
        `riche.append(person)`
`print(f"Nombre de personne qui gagne plus de 2000$ : {len(riche)}")`

#Nombre de personnes qui aiment les Drama 
`drama_lover = []`
`for person in people:`
    `films = person["pref_movie"]`
    `films_converti = films.replace("|","")`
    `if films == "Drama":`
        `drama_lover.append(person)`
`print(f"Nombre de personnes qui aiment les Drama : {len(drama_lover)}")`

### LIEN DEPÔT
[Lien vers exercice]()
