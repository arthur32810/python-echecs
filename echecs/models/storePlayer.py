from echecs.models.player import Player


class StorePlayer:

    def __init__(self):
        self.players = []

    # def add_player(self, id, first_name, last_name, birthday):
    #     """Enregistre un joueur dans le store"""

    #     self.players.append(Player(id, first_name, last_name, birthday))

    def add_player(self, player):
        """Enregistre un joueur dans le store"""

        self.players.append(player)

    def get_players(self):
        return self.players
