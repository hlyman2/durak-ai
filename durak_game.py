from cards import *
from utils import *
import random

class Field:
    def __init__(self):
        self.cards = {}

    def add_allegation(self, card):
        self.cards.update({card: None})

    def beat(self, allegation, card):
        self.cards.update({allegation: card})

    def unbeaten(self):
        unbeaten = []
        for card in self.cards:
            if self.cards[card] == None:
                unbeaten.append(card)

        return unbeaten

    def is_empty(self):
        return self.cards.is_empty()

class Player:
    def __init__(self):
        self.hand = []
        score = 0

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, num): # removes the card that you want to play from your hand and returns the card that you played
        removed = self.hand.remove(num)
        return removed

    def isOut(self)
        if not hand:
            score()
            return True
        else:
            return False

    def continue_game(self):
        players_in = 0
        for Player in players:
            if not Player.isOut(): 
                players_in += 1
        if players_in > 1:
            return True
        else:
            return False
    
    def score(self):
        self.score = scores.pop()

    def select_attacking_cards(self, field):
        if field.is_empty(): # initial attack
            
        
    def select_defending_cards(self, field):

class Play:
    def can_beat(self, card, allegation):
        return (
            (card.suit == allegation.suit and card.value > allegation.value)
            or (card.suit == self.trump_suit and allegation.suit != self.trump_suit)
        )

    def can_play(self, check)
        first = arr[0].getValue()
        return all(x.getValue() == first for x in check)



    def __init__(self):
        self.deck = Deck()
        self.deck.fill_small()
        self.deck.shuffle()
        self.players = [Player(), Player(), Player(), Player()]
        self.trump_suit = self.deck.last().suit

        self.victim = 0
        self.curr_player = 0
        scores = [3, 2, 1, 0]

        # deal 6 cards to each player
        for player in self.players:
            for i in range(6):
                player.add_card(self.deck.draw())
    
    def turn(self):
        attacker = self.victim
        self.victim = self.next_player(self.victim)

    def next_player(self, curr_player):
        if curr_player >= len(self.players) - 1:

    def next_player(self):
        if players(curr_player + 1).isOut():
            curr_player += 1
        
        if curr_player = 3:
            curr_player = 0
        else:
            curr_player += 1


