from echecs.models.storePlayer import StorePlayer


class Tournament:

    MAX_ROUNDS = 4
    MAX_PLAYERS = 2

    def __init__(self, name, place, note="", start_date=None, end_date=None, rounds=None, players=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.note = note
        self.players = [players]

    def add_players(self, players):
        """Ajoute des joueurs au tournoi"""
        self.players = players

    def to_dict(self):
        """Convertit un objet Tournament en dictionnaire pour JSON"""

        id_players = [player.player_id for player in self.players]

        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "note": self.note,
            "players": id_players,
            "rounds": self.rounds,
        }

    @staticmethod
    def from_dict(data):
        """Recrée un objet Tournament à partir d'un dictionnaire"""

        if data["players"]:
            players = [StorePlayer().get_player_with_id(player) for player in data["players"]]
        else:
            players = []

        return Tournament(
            data["name"], data["place"], data["note"], data["start_date"], data["end_date"], data["rounds"], players
        )

    def __str__(self):
        return f"Le tournoi {self.name}, se déroulera à {self.place}, remarques : {self.note}"

    def __repr__(self):
        return (
            f"Tournoi( name: {self.name}, place : {self.place}, start_date : {self.start_date},"
            f" end_date : {self.end_date}, round : {self.round}, note : {self.note})"
        )
