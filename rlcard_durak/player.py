class DurakPlayer:

    def __init__(self, player_id, player_type):
        self.player_id = player_id
        self.hand = []
        self.hasScored = False
        self.player_type = player_type
        self.pickUpCards()

    def play_card(self, plCard): # removes the card that you want to play from your hand and returns the card that you played
        self.hand.remove(plCard)
        return plCard

    def isOut(self):
        if not self.hand:
            return True
        else:
            return False

    def pickUpCards(self):
        while len(self.hand) < 6 and self.deck:
            self.hand.append(self.deck.draw())

    def handLength(self):
        return len(self.hand)