class Round:

    def __init__(self, name, numero_round, matches=None, completed=None):
        self.name = name
        self.numero_round = numero_round
        self.matches = matches or []
        self.completed = completed or False
