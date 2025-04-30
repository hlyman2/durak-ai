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
        self.np_random.shuffle(shuffle_deck)
        self.deck = list(shuffle_deck)

    def deal_to_6(self, victim, player):
        while not self.deck.empty() and len(player.hand) < 6:
            player.hand.append(self.deck.pop())

