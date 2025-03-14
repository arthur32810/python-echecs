from echecs.models.player import Player


class StorePlayer:

    def __init__(self):
        self.players = []

    def add_player(self, player):
        """Enregistre un joueur dans le store"""

        # Met en capitalize les noms et prénoms
        player.first_name = player.first_name.capitalize()
        player.last_name = player.last_name.capitalize()

        self.players.append(player)

    def get_players(self):
        return self.players

    def get_player_with_id(self, id_player):
        return next((player for player in self.players if player.player_id == id_player), None)

    def to_dict(self):
        return [player.to_dict() for player in self.players]

    def from_dict(self, data):
        self.players = [Player.from_dict(player) for player in data]
