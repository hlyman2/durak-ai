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

def generate_legal_actions(field, hand, act_type):
    if act_type == "initial_attack":
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
        n_more_attacks = field.max_cards - len(field.cards)

        allowed = []

        for i in range(n_more_attacks):
            for combo in combinations(attacking_cards, i):
                allowed.append(Action("attack", combo))

        return allowed
        
    if act_type == "defense":
        allowed = []
        unbeaten = []
        for a, b in field.cards.items():
            if b == None:
                unbeaten.update(a, [])

        for combo in combinations(hand, len(unbeaten)):
            match = beats(unbeaten, combo, field)
            if match != None:
                allowed.append(Action("defense", match))


def beats(attack, defence, field):
    if len(attack) != len(defense):
        return None

    match = [None] * len(defense)

    def backtrack(i):
        if i >= len(attack):
            return True
        atk = attack[i]
        for idx, df in enumerate(defense):
            if field.can_beat(atk, df) and df not in match:
                match[i] = df

                if backtrack(i+1):
                    return True
                else:
                    match[i] = None

    if backtrack(0):
        return None
