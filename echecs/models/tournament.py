class Tournament:

    def __init__(self, name, place, note=""):
        self.name = name
        self.place = place
        self.start_date = None
        self.end_date = None
        self.round = 4
        self.note = note

    def to_dict(self):
        """Convertit un objet Tournament en dictionnaire pour JSON"""
        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "round": self.round,
            "note": self.note,
        }

    @staticmethod
    def from_dict(data):
        """Recrée un objet Tournament à partir d'un dictionnaire"""
        return Tournament(
            data["name"], data["place"], data["start_date"], data["end_date"], data["round"], data["note"]
        )
