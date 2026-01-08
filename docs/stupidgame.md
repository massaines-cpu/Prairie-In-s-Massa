# [StuPid gAMe](index.md)

**Objectif** : Coder un jeu de cartes entre un humain et un robot, puis intégrer une stratégie de jeu dans le système pour faire en sorte que l'humain ou le robot gagne à chaque fois

## DP strategy
### Définir les fonctions
#### Pour la valeur des cartes

```python
class Carte:
    def __init__(self, value, shape):
        self.value = value
        self.shape = shape
    def __str__(self):
        return self.shape + str(self.value)
    def getValue(selfself):
        return self.value
```
#### Pour les données des joueurs
```python
class Player:
    def __init__(self, name : str, strategy):
        self.name = name
        self.hand = []
        self.strategy = strategy
    def __str__(self):
        return self.name + ": " + str([str(carte) for carte in self.hand])
    # def play(self):
    #     return self.hand.pop(-1)
    def play(self):
        return self.strategy(self.hand)
```
### Code pour créer le jeu sans stratégie
```python
from card import Carte
from player import Player
import random

def partie():
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
```
#### Pourcentage de victoire du robot
```python
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
```
#### Si on veut intégrer la stratégie des joueurs
```python
import random
from card import Card

def rand(hand):
    random.shuffle(hand)
    return hand.pop()

def plusGrande(hand, carte):
    hand.sort(key=lambda carte: carte.value)
    return hand.pop(-1)

def plusPetite(hand, carte):
    hand.sort(key=lambda carte: carte.value)
    return hand.pop()

def smart(hand, carte):
    if carte:
        hand.sort(key=lambda c: c.value)
        for c in hand:
            if c.value > carte.value:
                hand.remove(c)
                return c
    return plusPetite(hand, carte)
```
#### Code pour intégrer la stratégie des joueurs
```python
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
        return robot
    else:
        return humain
# card.py

class Card:
    def __init__(self, value: int, shape: str):
        self.value = value
        self.shape = shape

    def getValue(self):
        return self.value

    def __str__(self):
        return self.shape + str(self.value)
```
## Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-Ines-Massa/tree/initiale/stupidcard)