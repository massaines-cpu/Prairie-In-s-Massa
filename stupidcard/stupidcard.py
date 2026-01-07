from card import Carte
from player import Player
from strategy import rand
import random

# def partie():
def rand():
    pioche = [
        Carte(0, 'R'),
        Carte(1, 'R'),
        Carte(2, 'R'),
        Carte(3, 'R'),
        Carte(4, 'R'),
        Carte(1, 'C'),
        Carte(2, 'C'),
        Carte(3, 'C'),
        Carte(4, 'C'),
        Carte(5, 'C')
    ]
    assert len(pioche) == 10
    random.shuffle(pioche)
    humain = Player('humain', rand)
    robot = Player('robot', rand)

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
nb_parties = 10000

for i in range(nb_parties):
    # gagnant = partie()
    gagnant = partie(rand, rand)
    if gagnant == 'robot':
        victoires_robot += 1
taux = (victoires_robot / nb_parties) * 100
print(f"Sur {nb_parties} parties, le robot a gagné {victoires_robot} fois.")
print(f"Taux de victoire du robot : {taux}%")

#Définissez une stratégie qui consiste à jouer toujours sa “plus grosse” carte et
# utilisez là pour l’humain ou le robot, ou les deux.
# carte_max = 6
# humain = Player('humain')
# robot = Player('robot')
# carte_humain = humain.play()
# carte_robot = robot.play()
#
# if carte_max -1 > carte_robot.value:
#     carte_max = carte_robot.value
#     if carte_robot.value >= carte_humain.value:
#         point_robot += 1
#     else:
#         point_humain += 1
#
# if point_robot >= 3:
#     return 'robot'
# else:
#     return 'humain'

