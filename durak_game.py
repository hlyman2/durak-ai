from cards import *
from utils import *
import random

class Field:
    def can_beat(self, card, allegation):
        return (
            (card.suit == allegation.suit and card.value > allegation.value)
            or (card.suit == self.trump_suit and allegation.suit != self.trump_suit)
        )

    def __init__(self, trump, max_cards):
        self.cards = {}
        self.max_cards = max_cards
        self.trump_suit = trump

    # returns `False` if illegal
    def add_allegation(self, card):
        legal = False
        if self.cards.empty():
            legal = True
        for a, b in self.cards.items():
            if a.value == card.value or b.value == card.value:
                legal = True

        if len(self.cards) >= self.max_cards:
            legal = False

        if legal:
            self.cards.update({card: None})
            return True
        else:
            return False

    # Returns `False` if illegal
    def beat(self, allegation, card):
        if self.can_beat(card, allegation) and self.cards[allegation] == None:
            self.cards.update({allegation: card})
            return True
        else:
            return False

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
        self.hasScored = False

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, num): # removes the card that you want to play from your hand and returns the card that you played
        removed = self.hand.remove(num)
        return removed

    def isOut(self):
        if not self.hand:
            self.score()
            return True
        else:
            return False

    # Return `False` to pick up the cards, otherwise add cards to the field to defend
    def defend():
        return False

    # Add cards to the field to attack, return `False` to pass
    def attack():
        return False

    def pickUpCards(self):
        while len(self.hand) < 6 and self.deck:
            self.hand.append(self.deck.pop())

    def handLength(self):
        return len(self.hand)

class Play:
    def can_play(self, check):
        first = check[0].getValue()
        return all(x.getValue() == first for x in check)

    def continue_game(self):
        players_in = 0
        for p in self.players:
            if not p.isOut(): 
                players_in += 1
        return players_in > 1

    def __init__(self):
        self.deck = Deck()
        self.deck.fill_small()
        self.deck.shuffle()
        self.players = [Player(), Player(), Player(), Player()]
        self.trump_suit = self.deck.last().suit

        self.victim = 0
        self.curr_player = 0
    
    def turn(self):
        attacker = self.victim
        self.victim = self.next_player(self.victim)

    # returns the next alive player in order after `curr_player`
    def next_player(self, curr_player):
        new = curr_player + 1
        while self.players[new].isOut():
            if new >= len(self.players) - 1:
                new = 0
            else:
                new += 1

        return new

    # returns the player behind curr_player
    def last_player(self, )
        new = curr_player + 1
        while self.players[new].isOut():
            if new < 0:
                new = len(self.players) - 1
            else:
                new -= 1

        return new

    def deal_cards(self, victim):
        order = self.players
        last = order.remove(victim)
        order.append(last)
        for Player in order:
            Player.pickUpCards()



    def next_turn(self):
        
