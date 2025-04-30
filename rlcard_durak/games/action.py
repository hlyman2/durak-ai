from itertools import combinations
from rlcard.games.base import Card

class Action:
    '''
    act_type: either "attack", "initial_attack", or "defense"
    data: array of used cards
    '''
    def __init__(self, act_type, data):
        self.act_type = act_type
        self.data = data


