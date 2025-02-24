class Match:

    def __init__(self, player1, player2, score_player1=None, score_player2=None):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = score_player1 or 0
        self.score_player2 = score_player2 or 0

    def __str__(self):
        return (
            f"{self.player1.name} {self.player1.first_name} {self.player1.player_id} - "
            f"{self.player2.name} {self.player2.first_name} {self.player2.player_id}"
        )
