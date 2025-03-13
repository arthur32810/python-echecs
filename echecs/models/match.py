class Match:

    def __init__(self, player1, player2, score_player1=None, score_player2=None):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
    
    @property
    def is_finished(self):
        return self.score_player1 is not None and self.score_player2 is not None

    def player1_win(self):
        self.score_player1 = 1
        self.score_player2 = 0

    def player2_win(self):
        self.score_player1 = 0
        self.score_player2 = 1

    def match_nul(self):
        self.score_player1 = 0.5
        self.score_player2 = 0.5

    @property
    def winner(self):
        if self.score_player1 > self.score_player2:
            return self.player1
        elif self.score_player1 < self.score_player2:
            return self.player2
        elif self.score_player1 == self.score_player2:
            return 'Match nul'
        else:
            return None
        

    def __str__(self):
        return (
            f"{self.player1.last_name} {self.player1.first_name} {self.player1.player_id} - "
            f"{self.player2.last_name} {self.player2.first_name} {self.player2.player_id}"
        )

    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            'player1': self.player1,
            'player2': self.player2,
            'score_player1': self.score_player1,
            'score_player2': self.score_player2
        }
    
    def from_dict(self, data):
        return Match(data['player1'], data['player2'], data['score_player1'], data['score_player2'])