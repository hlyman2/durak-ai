from copy import deepcopy
import numpy as np

from .dealer import *
from .player import *
from .judger import *
from .action import *

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

        '''
        for i in range(self.num_players):
            self.players[i].status, self.players[i].score = self.judger.judge_round(self.players[i])
        '''

        self.winner = {}
        for i in range(self.num_players):
            self.winner['player' + str(i)] = 0

        self.history = []
        self.game_pointer = 0

        return self.get_state(self.game_pointer), self.game_pointer

    def step(self, action):
        '''
        if self.allow_step_back:
            p = deepcopy(self.players[self.game_pointer])
            d = deepcopy(self.dealer)
            w = deepcopy(self.winner)
            self.history.append((d, p, w))
        '''

        next_state = {}
        # Play hit
        if action != "stand":
            self.dealer.deal_card(self.players[self.game_pointer])
            self.players[self.game_pointer].status, self.players[self.game_pointer].score = self.judger.judge_round(
                self.players[self.game_pointer])
            if self.players[self.game_pointer].status == 'bust':
                # game over, set up the winner, print out dealer's hand # If bust, pass the game pointer
                if self.game_pointer >= self.num_players - 1:
                    while self.judger.judge_score(self.dealer.hand) < 17:
                        self.dealer.deal_card(self.dealer)
                    self.dealer.status, self.dealer.score = self.judger.judge_round(self.dealer)
                    for i in range(self.num_players):
                        self.judger.judge_game(self, i) 
                    self.game_pointer = 0
                else:
                    self.game_pointer += 1

                
        elif action == "stand": # If stand, first try to pass the pointer, if it's the last player, dealer deal for himself, then judge game for everyone using a loop
            self.players[self.game_pointer].status, self.players[self.game_pointer].score = self.judger.judge_round(
                self.players[self.game_pointer])
            if self.game_pointer >= self.num_players - 1:
                while self.judger.judge_score(self.dealer.hand) < 17:
                    self.dealer.deal_card(self.dealer)
                self.dealer.status, self.dealer.score = self.judger.judge_round(self.dealer)
                for i in range(self.num_players):
                    self.judger.judge_game(self, i) 
                self.game_pointer = 0
            else:
                self.game_pointer += 1


            
            

        hand = [card.get_index() for card in self.players[self.game_pointer].hand]

        if self.is_over():
            dealer_hand = [card.get_index() for card in self.dealer.hand]
        else:
            dealer_hand = [card.get_index() for card in self.dealer.hand[1:]]

        for i in range(self.num_players):
            next_state['player' + str(i) + ' hand'] = [card.get_index() for card in self.players[i].hand]
        next_state['dealer hand'] = dealer_hand
        next_state['actions'] = ('hit', 'stand')
        next_state['state'] = (hand, dealer_hand)

        

        return next_state, self.game_pointer

    def step_back(self):
        raise NotImplementedError

    def get_num_players(self):
        return self.num_players

    def get_num_actions(self):
        ''' Return the number of applicable actions

            number_of_actions (int)
        '''
        return 4 #Check this, could be returning the wrong number


    def get_player_id(self):
        ''' Return the current player's id

        Returns:
            player_id (int): current player's id
        '''
        return self.game_pointer

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
        state['actions'] = ('hit', 'stand')
        hand = [card.get_index() for card in self.players[player_id].hand]
        if self.is_over():
            dealer_hand = [card.get_index() for card in self.dealer.hand]
        else:
            dealer_hand = [card.get_index() for card in self.dealer.hand[1:]]

        for i in range(self.num_players):
            state['player' + str(i) + ' hand'] = [card.get_index() for card in self.players[i].hand]
        state['dealer hand'] = dealer_hand
        state['state'] = (hand, dealer_hand)

        return state

    # done
    def is_over(self):
        for i in range(self.num_players):
            if self.winner['player' + str(i)] == 0:
                return False

        return True
