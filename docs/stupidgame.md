# [Jeu robot humain](index.md)

**Objectif** : Coder un jeu de cartes entre un humain et un robot, puis intégrer une stratégie de jeu dans le système pour faire en sorte que l'humain ou le robot gagne à chaque fois

## DP strategy
### Définir les fonctions
#### Pour la valeur des cartes

```python
class Carte: #represente une carte du jeu
    def __init__(self, value, shape):
        self.value = value   #chaque carte contient ces 2 informations
        self.shape = shape
    def __str__(self):
        return self.shape + str(self.value) #lisibilité, R3 OU C1
    def getValue(selfself):
        return self.value #on a la valeur de la carte
```
#### Pour les données des joueurs
```python
class Player: #classe du joueur, donc ses infos
    def __init__(self, name : str, strategy):
        self.name = name #humain ou robot
        self.hand = []  #cartes dans la main
        self.strategy = strategy #strat pour quelle carte jouer
    def __str__(self):
        return self.name + ": " + str([str(carte) for carte in self.hand]) #visibilité sur nom joueur + ses cartes
    def play(self):
        return self.hand.pop(-1) #aleatoire
    def play(self): #soit l'un ou l'autre par contre
        return self.strategy(self.hand) #on integre strat

```
### Code pour créer le jeu sans stratégie (au hasard)
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
    robot = Player('robot', rand) #mode alearoire

    while len(pioche): #distribution
        carte = pioche.pop(-1)
        humain.hand.append(carte)
        carte = pioche.pop(-1)
        robot.hand.append(carte)
    print(robot)
    print(humain)

    point_robot = 0
    point_humain = 0
    for tour in range(5): #5tours
        carte_humain = humain.play()
        carte_robot = robot.play()

        if carte_robot.value >= carte_humain.value: #on compare
            point_robot += 1
        else:
            point_humain += 1

    if point_robot >= 3: #joueur qui gg en moins de 3 manches
        return 'robot'
    else:
        return 'humain'
```
#### Pourcentage de victoire du robot
```python
victoires_robot = 0
nb_parties = 10000 #plus c'est eleve + c'est fiable

for i in range(nb_parties):
    gagnant = partie()
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
    return hand.pop() #bon la c'est la strat pas strat, uniquement aleatoire

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
            if c.value > carte.value: #sadapte en fonction adversaire, si cette carte alors joue celle la
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


def partie(strategy_humain, strategy_robot): #choix de strat pour chaque joueur
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
        carte_du_robot = robot.play() #lerobot joue en premier
        carte_de_humain = humain.play(carte_du_robot) #lhumain joue en fonction du coup
        if carte_du_robot.value >= carte_de_humain.value:
            points_du_robot += 1
    # victoire
    if points_du_robot >= 3:
        return robot
    else:
        return humain
```
## Lien dépôt
[Lien vers exercice](https://github.com/massaines-cpu/Prairie-Ines-Massa/tree/initiale/stupidcard)