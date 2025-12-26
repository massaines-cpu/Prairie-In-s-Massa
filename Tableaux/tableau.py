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
    groupe = prenoms[i:i+k]
    groupes.append(groupe)
    i = i + k

print(groupes)
