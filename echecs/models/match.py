class Match:

    def __init__(self, player1, player2, score_player1=None, score_player2=None):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1
        self.score_player2 = score_player2
    
    @property
    def is_finished(self):
        return self.score_player1 is not None and self.score_player2 is not None

    def __str__(self):
        return (
            f"{self.player1.last_name} {self.player1.first_name} {self.player1.player_id} - "
            f"{self.player2.last_name} {self.player2.first_name} {self.player2.player_id}"
        )
