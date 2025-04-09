import random
from utils import *

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def num():  # return number for neural network
        return ...

    def getSuit(self):
        return SUITS[self.suit]
    def getValue(self):
        return VALUES[self.value]

class Deck:
    def __init__(self):
        self.cards = []
   
    # fill with a full deck
    def fill(self):
        for suit in SUITS.keys():
            for value in VALUES.keys():
                self.cards.append(Card(suit, value))

    # fill with a small deck (2-5 removed)
    def fill_small(self):
        for suit in SUITS.keys():
            for value in range(6, 14+1):
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
