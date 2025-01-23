from echecs.models.player import Player


class StorePlayer:

    def __init__(self, save_callback=None):
        self.players = []
        self.save_callback = save_callback

    def add_player(self, player):
        """Enregistre un joueur dans le store"""
        self.players.append(player)

        if self.save_callback:
            self.save_callback()

    def get_players(self):
        return self.players

    def to_dict(self):
        return [player.to_dict() for player in self.players]

    def from_dict(self, data):
        self.players = [Player.from_dict(player) for player in data]
