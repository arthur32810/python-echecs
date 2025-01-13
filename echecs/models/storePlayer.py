from echecs.models.player import Player


class StorePlayer:

    def __init__(self):
        self.players = []

    def add_player(self, first_name, last_name, birthday):
        """Enregistre un joueur dans le store"""

        self.players.append(Player(first_name, last_name, birthday))

    def get_players(self):
        return self.players
