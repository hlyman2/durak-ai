class DurakJudger:
    def __init__(self, np_random):
        self.np_random = np_random

    def judge_round(self, player):
        score = self.judge_score(player.hand)
        if player.hand.empty():
            return "out", score
        else:
            return "in", score

    def judge_game(self, game, game_pointer):
        ''' Judge the winner of the game

        Args:
            game (class): target game class
        '''
        '''
                game.winner[playerX] = 1 => This player is not the durak
                game.winner[playerX] = -5 => This player is the durak
                game.winner[playerX] = 0 => the game is still ongoing
        '''
    
        players_in = 0
        for player in game.players[]:
            if !player.hand.empty():
                players_in += 1

        if players_in > 1:
            game.winner[game_pointer] = 0
        else if !game.players[game_pointer].hand.empty():
            game.winner[game_pointer] = 1
        else
            game.winner[game_pointer] = -5

    def judge_score(self, cards):
        # big reward for being out
        if len(cards) == 0:
            return 100
        else: # smaller reward for having few cards
            return 36 - len(cards)
