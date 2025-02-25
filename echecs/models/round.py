class Round:

    def __init__(self, name, numero_round, matches=None, completed=None):
        self.name = name
        self.numero_round = numero_round
        self.matches = matches or []

    @property  
    def is_finished(self):
        return all(match.is_finished for match in self.matches)

    def __repr__(self):
        return f"{self.name} {self.numero_round}"