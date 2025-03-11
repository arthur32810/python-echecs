class Round:

    def __init__(self, name, numero_round, matches=None, start_time=None, end_time=None):
        self.name = name
        self.numero_round = numero_round
        self.matches = matches or []
        self.start_time = start_time
        self.end_time = end_time 

    @property  
    def is_finished(self):
        return all(match.is_finished for match in self.matches)

    def __repr__(self):
        return f"{self.name} {self.numero_round}"