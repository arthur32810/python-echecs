from datetime import datetime
from echecs.models.match import Match
from echecs.models.round import Round


class Tournament:

    def __init__(self, name, place, note="", start_date=None, end_date=None, rounds=None, players=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds or []
        self.note = note
        self.players = players or []

    def start_tournament(self):
        """Lance le tournoi"""
        self.start_date = datetime.now()

        match1 = Match(self.players[0], self.players[1])
        match2 = Match(self.players[2], self.players[3])
        match3 = Match(self.players[4], self.players[5])
        match4 = Match(self.players[6], self.players[7])

        round = Round("round1", 1)
        round.matches = [match1, match2, match3, match4]
        self.rounds.append(round)

    def next_round(self):
        """Passe au prochain round"""
        pass

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
    def from_dict(data, store):
        """Recrée un objet Tournament à partir d'un dictionnaire"""

        if data["players"]:

            players = [store.players.get_player_with_id(player) for player in data["players"]]

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
