# Exercice tableau groupes

Objectif : Créer des sous groupes avec tous les prénoms repartis de manière aléatoire.

## Version Python
> **Note :** pour aleatoire
`import random`
`prenoms = ["Inès", "Asma", "Khrisly", "Yacine", "Ludovic", "Manon", "Lilian", "Manar", "Ahmadola", "Noemie", "Danitza" ]`

> **Note :** vide pour l'instant
`groupes = []`

> **Note :** vide pour l'instant bim les prenoms vont etre melangés

> **Note :** les prenoms vont etre melangés
`random.shuffle(prenoms)`

> **Note :** test groupe de 4 personnes
`k = 4`

> **Note :** on part de 0, pas de doublon
`i = 0`

> **Note :** boucle
`while i < len(prenoms):`
    `groupe = prenoms[i:i+k]`
    `groupes.append(groupe)`
    `i = i + k`

`print(groupes)`



### LIEN DEPÔT
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-In-s-Massa/tree/initiale/Tableaux)
