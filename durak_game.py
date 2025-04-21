from cards import *
from utils import *
import random
import human
import bot

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

    def remove_all_cards(self):
        cards = []
        for l, r in self.cards.items():
            cards.append(l)
            cards.append(r)
        self.cards = {}
        return cards

    def is_empty(self):
        return self.cards.is_empty()

class Player:
    def __init__(self, player_type):
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

    # Return `False` to pick up the cards, otherwise add cards to the field to defend
    def defend(self, field):
        if self.player_type = PLAYER_HUMAN:
            return human.defend(self.hand, field)
        else if self.player_type = PLAYER_BOT:
            return bot.defend(self.hand, field)

    # Add cards to the field to attack, return `False` to pass
    def attack(self, field):
        if self.player_type = PLAYER_HUMAN:
            return human.attack(self.hand, field)
        else if self.player_type = PLAYER_BOT:
            return bot.attack(self.hand, field)

    def pickUpCards(self):
        while len(self.hand) < 6 and self.deck:
            self.hand.append(self.deck.draw())

    def handLength(self):
        return len(self.hand)
    

class Play:
    def can_play(self, check):
        first = check[0].getValue()
        return all(x.getValue() == first for x in check)

    def count_players(self):
        players_in = 0
        for p in self.players:
            if not p.isOut(): 
                players_in += 1

        return players_in


    def continue_game(self):
        return self.count_players() > 1

    def __init__(self):
        self.deck = Deck()
        self.deck.fill_small()
        self.deck.shuffle()
        self.players = [Player(self.deck), Player(self.deck), Player(self.deck), Player(self.deck)]
        self.trump_suit = self.deck.last().suit

        self.victim = 0
        self.curr_player = 0
    
    def turn(self):
        attacker = self.victim
        self.victim = self.next_player(self.victim)

    # returns the next alive player in order after `curr_player`
    def next_player(self, curr_player):
        new = curr_player + 1
        if new > len(self.players) - 1:
            new = 0

        while self.players[new].isOut():
            if new >= len(self.players) - 1:
                new = 0
            else:
                new += 1

        return new

    # returns the player behind curr_player
    def last_player(self, curr_player):
        new = curr_player - 1
        if new < 0:
            new = len(self.players) - 1
        while self.players[new].isOut():
            if new < 0:
                new = len(self.players) - 1
            else:
                new -= 1

        return new

    def deal_cards(self, victim):
        for player in self.players:
            if not player.isOut() and not player == victim:
                player.pickUpCards()
        if not victim.isOut():
            victim.pickUpCards()
        
        
        '''
        order = self.players
        order.remove(victim)
        order.append(victim)
        for player in order:
            if not player.isOut():
                player.pickUpCards()
        '''

    def next_turn(self):
        self.deal_cards(self.players[self.victim])

        print(self.victim, self.curr_player)

        self.victim = self.next_player(self.victim)
        
        curr_player = self.last_player(self.victim)

        n_skipped = 0

        self.field = Field(self.trump_suit, min(6, len(self.players[self.victim].hand)))

        while True:
            if curr_player == self.victim:
                if self.players[curr_player].defend(self.field) == False:
                    self.players[curr_player].cards.join(self.field.remove_all_cards())
                    break
                else:
                    n_skipped = 0
            else:
                if self.players[curr_player].attack(self.field) == False:
                    n_skipped += 1
                else:
                    n_skipped = 0

            while n_skipped < self.count_players() - 1 and !self.field.unbeaten().empty():
                 if self.players[curr_player].defend(self.field) == False:
                    self.players[curr_player].cards.join(self.field.remove_all_cards())

            while n_skipped < self.count_players() - 1 and  not self.field.unbeaten():
                 if self.players[curr_player].defend() == False:
                    self.players[curr_player].hand.append(self.field.remove_all_cards())
                    break

            curr_player = self.next_player(self.victim)

