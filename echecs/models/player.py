class Player:

    def __init__(self, player_id, first_name, last_name, birthday):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def to_dict(self):
        """Convertit un objet Player en dictionnaire pour JSON"""
        return {
            "player_id": self.player_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthday": self.birthday,
        }

    @staticmethod
    def from_dict(data):
        """Recrée un objet Player à partir d'un dictionanire"""

        return Player(data["player_id"], data["first_name"], data["last_name"], data["birthday"])

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Identifiant : {self.player_id}"

    def __repr__(self):
        return (
            f"Joueur( player_id: {self.player_id}, first_name : {self.first_name}, last_name : {self.last_name},"
            f" birdthay : {self.birthday})"
        )
