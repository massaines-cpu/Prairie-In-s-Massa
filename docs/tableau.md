# [Exercice tableau groupes](index.md)

Objectif : Créer des sous groupes avec tous les prénoms repartis de manière aléatoire.

## Version Python

```python
import random
#pour aleatoire
prenoms = ["Inès", "Asma", "Khrisly", "Yacine", "Ludovic", "Manon", "Lilian", "Manar", "Ahmadola", "Noemie", "Danitza" ]

groupes = []
#vide pour l'instant
random.shuffle(prenoms)
#bim les prenoms vont etre melangés
k = 4
#test groupe de 4 personnes
i = 0
#on part de 0
#pas de doublon
while i < len(prenoms):
    groupe = prenoms[i:i+k] #prend ls 4 personnes suivant dans la liste
    groupes.append(groupe) #ajout
    i += k # on avance de 4 pour prochain groupe

print(groupes)

```


### Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-In-s-Massa/tree/initiale/Tableaux)
