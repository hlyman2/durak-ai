class Field:
    def can_beat(self, card, allegation):
        return (
            (card.suit == allegation.suit and rank2int(card.rank )> rank2int(allegation.rank))
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
            if a.rank == card.rank or b.rank == card.rank:
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

    def remove_all_cards(self):
        cards = []
        for l, r in self.cards.items():
            cards.append(l)
            cards.append(r)
        self.cards = {}
        return cards

    def is_empty(self):
        return self.cards.is_empty()
