from echecs.models.match import Match
from datetime import datetime


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
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None
        }
    
    def from_dict(round, store):
        matches = [Match.from_dict(match, store) for match in round['matches']]

        return Round(
            round['name'], 
            round['numero_round'], 
            matches, 
            datetime.fromisoformat(round['start_time']) if round['start_time'] else None, 
            datetime.fromisoformat(round['end_time']) if round['end_time'] else None
        )