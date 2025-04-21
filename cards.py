import random
from utils import *

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def num(self):  # return number for neural network
        return ...

    def __str__(self):
        return f"{self.getValue()} {self.getSuit()}"
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit


class Deck:
    def __init__(self):
        # index `0` is the bottom of the deck
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

    def last(self):
        return self.cards[0]

