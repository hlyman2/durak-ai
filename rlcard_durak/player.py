class DurakPlayer:

    def __init__(self, player_id, np_random):
        self.player_id = player_id
        self.hand = []
        self.score = 0

    def get_player_id(self):
        return self.player_id
