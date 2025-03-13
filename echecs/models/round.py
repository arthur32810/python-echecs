from echecs.models.match import Match


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
    
    def to_dict(self):
        matches = [match.to_dict() for match in self.matches]
        return {
            'name': self.name,
            'numero_round': self.numero_round,
            'matches': matches,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
    
    def from_dict(self, data):
        matches = [Match().from_dict(match) for match in data['matches']]
        
        return Round(data['name'], data['numero_round'], matches, data['start_time'], data['end_time'])