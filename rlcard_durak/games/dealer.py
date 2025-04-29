from rlcard_durak.utils.utils import init_standard_deck
import numpy as np
from rlcard_durak.games.player import *


class DurakDealer:
    ''' Initialize a GinRummy dealer class
    '''
    def __init__(self, players):
        ''' Empty discard_pile, set shuffled_deck, set stock_pile
        '''
        self.deck = init_standard_deck()
        self.shuffle()

    def shuffle(self):
        ''' Shuffle the deck
        '''
        shuffle_deck = np.array(self.deck)
        np.random.shuffle(shuffle_deck)
        self.deck = list(shuffle_deck)

    def deal_cards(self, victim, players):
        ''' Deal some cards from stock_pile to one player

        Args:
            player (GinRummyPlayer): The GinRummyPlayer object
            num (int): The number of cards to be dealt
        '''
        for player in players:
            if not player.isOut() and not player == victim:
                player.pickUpCards()
        if not victim.isOut():
            victim.pickUpCards()