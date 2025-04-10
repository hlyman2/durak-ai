from cards import *
from utils import *

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
        self.curr_player = 0
        scores = [3, 2, 1, 0]

        # deal 6 cards to each player
        for player in self.players:
            for i in range(6):
                player.add_card(self.deck.draw())
    
    def get_player(self):
        return curr_player

    def next_player(self):
        if players(curr_player + 1).isOut():
            curr_player += 1
        
        if curr_player = 3:
            curr_player = 0
        else:
            curr_player += 1
