from copy import deepcopy
import numpy as np

from .dealer import *
from .player import *
from .judger import *
from .action import *
from .field import *

class DurakGame:
    def __init__(self, allow_step_back=False):
        ''' Initialize the class Durak Game
        '''
        self.allow_step_back = allow_step_back
        self.np_random = np.random.RandomState()


    def configure(self, game_config):
        self.num_players = game_config['game_num_players']
        self.num_decks = game_config['game_num_decks']

    def init_game(self):
        self.players = []
        for i in range(self.num_players):
            self.players.append(DurakPlayer(i, self.np_random))
        
        self.dealer = DurakDealer(self.players)
        self.judger = DurakJudger(self.np_random)
        
        self.field = Field(self.dealer.getTrump(), 6)

        self.victim = 1
        self.game_pointer = 0
        self.n_skipped = 0

        '''
        for i in range(self.num_players):
            self.players[i].status, self.players[i].score = self.judger.judge_round(self.players[i])
        '''

        self.winner = {}
        for i in range(self.num_players):
            self.winner['player' + str(i)] = 0

        self.history = []

        return self.get_state(self.game_pointer), self.game_pointer

    def step(self, action):
        '''
        if self.allow_step_back:
            p = deepcopy(self.players[self.game_pointer])
            d = deepcopy(self.dealer)
            w = deepcopy(self.winner)
            self.history.append((d, p, w))
        '''

        if action.act_type == "initial_attack":
            for card in action.data:
                self.players[self.game_pointer].hand.remove(card)
                self.field.add(card)
            self.game_pointer = self.next_player(self.game_pointer)

        if action.act_type == "attack":
            if action.data.empty():
                n_skipped += 1
                if n_skipped >= self.count_players() - 1 and self.field.unbeaten().empty():
                    # allegations beat
                    self.iterate_victim()
                else:
                    self.game_pointer = self.next_player(self.game_pointer)
            else:    
                n_skipped = 0
                for card in action.data:
                    self.players[self.game_pointer].hand.remove(card)
                    self.field.add(card)
                self.game_pointer = self.next_player(self.game_pointer)

        if action.act_type == "defense":
            self.n_skipped = 0

            if action.data.empty(): # pick up cards
                self.players[self.gamer_pointer].cards.join(self.field.remove_all_cards())
                self.iterate_victim()
                self.iterate_victim()
            else:
                unbeaten = self.field.unbeaten()
                beat = beats(unbeaten, action.data, self.field)
                for i in range(self.field.unbeaten()):
                    self.field[unbeaten[i]] = beat[i]
                    self.players[self.game_pointer].hand.remove(beat[i])

                if len(self.field.cards) >= self.field.max_cards: # allegations beat
                    self.iterate_victim()
                else:
                    self.game_pointer = self.next_player(self.game_pointer)

        return self.get_state(self.game_pointer), self.game_pointer

    def iterate_victim(self):
        for i in 0..len(self.players):
            if i != self.victim:
                self.dealer.deal_to_6(self.players[i])
        self.dealer.deal_to_6(self.players[self.victim])

        self.victim = self.next_player(self.victim)
        
        self.game_pointer = self.last_player(self.victim)

        n_skipped = 0

        self.field = Field(self.trump_suit, min(6, len(self.players[self.victim].hand)))

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



    def step_back(self):
        raise NotImplementedError

    def get_num_players(self):
        return self.num_players

    def get_num_actions(self):
        ''' Return the number of applicable actions

            number_of_actions (int)
        '''
        return 37


    def get_player_id(self):
        ''' Return the current player's id

        Returns:
            player_id (int): current player's id
        '''
        return self.game_pointer

    # State is what is known to the agent????
    def get_state(self, player_id):
        ''' Return player's state

        Args:
            player_id (int): player id

        Returns:
            state (dict): corresponding player's state
        '''
        '''
                before change state only have two keys (action, state)
                but now have more than 4 keys (action, state, player0 hand, player1 hand, ... , dealer hand)
                Although key 'state' have duplicated information with key 'player hand' and 'dealer hand', I couldn't remove it because of other codes
                To remove it, we need to change dqn agent too in my opinion
                ''' 
        state = {}
        state['field'] = self.field

        act_type = "attack"
        if player_id == self.victim:
            act_type = "defense"
        elif not state["field"]:
            act_type = "initial_attack"
        state['actions'] = generate_legal_actions(self.field, self.players[player_id].hand, act_type)

        # hand = [card.get_index() for card in self.players[player_id].hand]
        # if self.is_over():
        #     dealer_hand = [card.get_index() for card in self.dealer.hand]
        # else:
        #     dealer_hand = [card.get_index() for card in self.dealer.hand[1:]]

        # for i in range(self.num_players):
        #     state['player' + str(i) + ' hand'] = [card.get_index() for card in self.players[i].hand]
        # state['dealer hand'] = dealer_hand
        # state['state'] = (hand, dealer_hand)

        return state

    # done
    def is_over(self):
        for i in range(self.num_players):
            if self.winner['player' + str(i)] == 0:
                return False

        return True
    
    def getPlayerCards(self):
        return self.players[0].hand, self.players[1].hand, self.players[2].hand, self.players[3].hand
