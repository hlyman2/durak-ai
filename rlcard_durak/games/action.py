from itertools import combinations
from rlcard.games.base import Card

class Action:
    '''
    act_type: either "attack", "initial_attack", or "defense"
    data: if attack, array of attacking cards; if defense, dict of {allegation: beat} or empty to take cards
    '''
    def __init__(self, act_type, data):
        self.act_type = act_type
        self.data = data

def generate_legal_actions(field, hand, act_type):
    if act_type = "initial_attack":
        ranks = {}
        for rank in Card.valid_rank:
            ranks.update(rank, [])
        for card in hand:
            ranks[card.rank].append(card)

        allowed = []

        for rank in Card.valid_rank:
            for i in range(len(ranks[rank])):
                for combo in combinations(ranks[rank], i):
                    allowed.append(Action("initial_attack", combo))

        return allowed


    if act_type == "attack":
        rankset = set()
        for a, b in field.cards.items():
            rankset.add(a.rank)
            rankset.add(b.rank)
        attacking_cards = []
        for card in hand:
            if card.rank in rankset:
                attacking_cards.append(card)
        n_more_attacks = field.max_cards - len(fields.cards)

        allowed = []

        for i in range(n_more_attacks):
            for combo in combinations(attacking_cards, i):
                allowed.append(Action("attack", combo))

        return allowed
        
    if act_type == "defense":
        allowed = [{}]
        unbeaten = map()
        for a, b in field.cards.items():
            if b == None:
                unbeaten.update(a, [])
        
