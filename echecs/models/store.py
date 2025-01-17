import json

from echecs.models.storePlayer import StorePlayer
from echecs.models.storeTournament import StoreTournament


class Store:

    def __init__(self, storage_file="data.json"):
        self.storage_file = storage_file
        self.players = StorePlayer(save_callback=self.save_data)
        self.tournaments = StoreTournament(save_callback=self.save_data)
        self.load_data()

    def save_data(self):
        data = {"players": self.players.to_dict()}

        with open(self.storage_file, "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                self.players.from_dict(data.get("players", []))

        except FileNotFoundError:
            print("Fichier demandé non trouve")
