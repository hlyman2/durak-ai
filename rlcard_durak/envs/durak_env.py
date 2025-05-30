import numpy as np
from collections import OrderedDict

from rlcard.envs import Env
from rlcard_durak.games import Game

DEFAULT_GAME_CONFIG = {
        'game_num_players': 4,
        'game_num_decks': 1
        }

class DurakEnv(Env):
    ''' Blackjack Environment
    '''

    def __init__(self, config):
        ''' Initialize the Blackjack environment
        '''
        self.name = 'durak'
        self.default_game_config = DEFAULT_GAME_CONFIG
        self.game = Game()
        super().__init__(config)
        self.actions = ['attack', 'defend', 'take', 'stand']
        self.state_shape = [[4] for _ in range(self.num_players)]
        self.action_shape = [None for _ in range(self.num_players)]

    def _get_legal_actions(self):
        ''' Get all leagal actions

        Returns:
            encoded_action_list (list): return encoded legal action list (from str to int)
        '''
        encoded_action_list = []
        for i in range(len(self.actions)):
            encoded_action_list.append(i)
        return encoded_action_list

    def _extract_state(self, state):
        ''' Extract the state representation from state dictionary for agent

        Args:
            state (dict): Original state from the game

        Returns:
            observation (list): combine the player's score and dealer's observable score for observation
        '''
        player1_c, player2_c, player3_c, player4_c = self.game.getPlayerCards()

        player1_s = get_score(player1_c)
        player2_s = get_score(player2_c)
        player3_s = get_score(player3_c)
        player4_s = get_score(player4_c)


        obs = np.array([player1_s, player2_s, player3_s, player4_s])

        legal_actions = OrderedDict({i: None for i in range(len(self.actions))})
        extracted_state = {'obs': obs, 'legal_actions': legal_actions}
        extracted_state['raw_obs'] = state
        extracted_state['raw_legal_actions'] = [a for a in self.actions]
        extracted_state['action_record'] = self.action_recorder
        return extracted_state

    def get_payoffs(self):
        ''' Get the payoff of a game

        Returns:
           payoffs (list): list of payoffs
        '''
        payoffs = []

        for i in range(self.num_players):
            if self.game.winner['player' + str(i)] == 3:
                payoffs.append(2)  # Dealer bust or player get higher score than dealer
            elif self.game.winner['player' + str(i)] == 2:
                payoffs.append(1)  # Dealer and player tie
            elif self.game.winner['player' + str(i)] == 1:
                payoffs.append(0)
            else:
                payoffs.append(-1)  # Player bust or Dealer get higher score than player

        return np.array(payoffs)


    def _decode_action(self, action_id):
        ''' Decode the action for applying to the game

        Args:
            action id (int): action id

        Returns:
            action (str): action for the game
        '''
        return self.actions[action_id]

def get_score(hand):
    return 36 - len(hand)