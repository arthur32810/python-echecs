class Player:

    def __init__(self, id, first_name, last_name, birthday):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

    def to_dict(self):
        """Convertit un objet Player en dictionnaire pour JSON"""
        return {}

    def __str__(self):
        pass
