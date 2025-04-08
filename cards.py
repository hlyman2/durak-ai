import random
from utils import *

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def num():  # return number for neural network
        return ...
    def getSuit():
        SUITS[0]

class Deck:
    def __init__(self):
        self.cards = []
    
    def fill():
        for suit in SUITS.keys():
            for value in VALUES.keys():
                cards.append(Card(suit, value))
    
    def shuffle():
        random.shuffle(self.cards)

    def draw():
        return self.cards.pop()