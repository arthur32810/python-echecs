class Tournament:

    def __init__(self, name, place, note="", start_date=None, end_date=None, rounds=None, players=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.note = note
        self.players = [players]

    def to_dict(self):
        """Convertit un objet Tournament en dictionnaire pour JSON"""
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "note": self.note,
        }

    @staticmethod
    def from_dict(data):
        """Recrée un objet Tournament à partir d'un dictionnaire"""
        return Tournament(
            data["name"],
            data["place"],
            data["note"],
            data["start_date"],
            data["end_date"],
            data["rounds"],
            data["players"],
        )

    def __str__(self):
        return f"Le tournoi {self.name}, se déroulera à {self.place}, remarques : {self.note}"

    def __repr__(self):
        return (
            f"Tournoi( name: {self.name}, place : {self.place}, start_date : {self.start_date},"
            f" end_date : {self.end_date}, round : {self.round}, note : {self.note})"
        )
