#test autre code

import random
from card import Carte
from player import Player


def une_partie():
    pioche = [
        Carte(0, 'R'), Carte(1, 'R'), Carte(2, 'R'), Carte(3, 'R'), Carte(4, 'R'),
        Carte(1, 'C'), Carte(2, 'C'), Carte(3, 'C'), Carte(4, 'C'), Carte(5, 'C')
    ]
    random.shuffle(pioche)

    humain = Player('humain')
    robot = Player('robot')


    while len(pioche):
        carte = pioche.pop(-1)
        humain.hand.append(carte)
        carte = pioche.pop(-1)
        robot.hand.append(carte)
        print(robot)
        print(humain)

    point_robot = 0
    point_humain = 0

    for tour in range(5):
        carte_humain = humain.play()
        carte_robot = robot.play()

        if carte_robot.value >= carte_humain.value:
            point_robot += 1
        else:
            point_humain += 1

    if point_robot >= 3:
        return 'robot'
    else:
        return 'humain'


victoires_robot = 0
nb_parties = 1000

for i in range(nb_parties):
    gagnant = une_partie()
    if gagnant == 'robot':
        victoires_robot += 1

taux = (victoires_robot / nb_parties) * 100
print(f"Sur {nb_parties} parties, le robot a gagné {victoires_robot} fois.")
print(f"Taux de victoire du robot : {taux}%")