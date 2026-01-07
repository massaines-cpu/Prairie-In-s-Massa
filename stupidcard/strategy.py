#strat
import random
from card import Card

def rand(hand):
    random.shuffle(hand)
    return hand.pop()
def plusgrande(hand):
    hand.sort(key=lambda a, b: a.value - b.value)
    carte = max(hand)
