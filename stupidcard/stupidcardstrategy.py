import random
from card import Carte
from player import Player
from strategy import rand


def partie(strategy_humain, strategy_robot):
    # les cartes
    pioche = [
        Card(0, "R"),
        Card(1, "R"),
        Card(2, "R"),
        Card(3, "R"),
        Card(4, "R"),
        Card(1, "C"),
        Card(2, "C"),
        Card(3, "C"),
        Card(4, "C"),
        Card(5, "C"),
    ]
    # les joueurs
    humain = Player("Humain", strategy_humain)
    robot = Player("Robot", strategy_robot)
    # mélange
    random.shuffle(pioche)
    # distribution
    while len(pioche) > 0:
        carte = pioche.pop(-1)
        humain.hand.append(carte)
        carte = pioche.pop(-1)
        robot.hand.append(carte)

    # tours
    points_du_robot = 0
    for tour in range(5):
        carte_du_robot = robot.play()
        carte_de_humain = humain.play(carte_du_robot)
        if carte_du_robot.value >= carte_de_humain.value:
            points_du_robot += 1
    # victoire
    if points_du_robot >= 3:
        return 'robot'
    else:
        return 'humain'