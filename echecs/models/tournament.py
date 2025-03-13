from datetime import datetime
from echecs.models.match import Match
from echecs.models.round import Round


class Tournament:

    def __init__(self, name, place, note="", start_date=None, end_date=None, rounds=None, players=None, score=None):
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds or []
        self.note = note
        self.players = players or []
        self.score = score or {}

    def start_tournament(self):
        """Lance le tournoi"""
        self.start_date = datetime.now()
        self.init_score()
        self.init_round(len(self.rounds) + 1)
        self.generate_matchs_round()

    def next_round(self):
        """Passe au prochain round"""
        self.init_round(len(self.rounds) + 1)
        self.generate_matchs_round()
        
    def end_tournament(self):
        """Termine le tournoi"""
        self.end_date = datetime.now()

    def init_score(self):
        """Initialise le score des joueurs"""
        for player in self.players:
            self.score[player] = 0

    def init_round(self, numero_round):
        """Initialise les rounds"""
        round = Round(f"round{numero_round}", numero_round)
        self.rounds.append(round)
        

    def get_classement(self):
        """Renvoie le classement des joueurs"""
        return sorted(self.score.items(), key=lambda x: x[1], reverse=True)

    def generate_matchs_round(self):
        """Passe au prochain round"""
        available_players = self.get_classement()

        while available_players:
            first_player = available_players.pop(0)[0]
            
            for adversaire in available_players:
                if not self.has_played(first_player, adversaire[0]):
                    second_player = adversaire[0]
                    match = Match(first_player, second_player)
                    self.rounds[-1].matches.append(match)
                    available_players.remove(adversaire)
                    break

    def has_played(self, player1, player2):
        """Vérifie si deux joueurs se sont déjà affrontés"""
        for round in self.rounds:
            if round.numero_round == 1:
                return False
            
            for match in round.matches:
                if player1 in match.players and player2 in match.players:
                    return True
        return False
    
    def to_dict(self):
        """Convertit un objet Tournament en dictionnaire pour JSON"""

        id_players = [player.player_id for player in self.players]
        rounds = [round.to_dict() for round in self.rounds]

        score = {player.player_id: score for player, score in self.score.items()}

        return {
            "name": self.name,
            "place": self.place,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "note": self.note,
            "players": id_players,
            "rounds": rounds,
            "score": score
        }

    @staticmethod
    def from_dict(data, store):
        """Recrée un objet Tournament à partir d'un dictionnaire"""

        players = [store.players.get_player_with_id(player) for player in data["players"]]
        rounds = [Round.from_dict(round, store) for round in data["rounds"]]
        score = {store.players.get_player_with_id(player): score for player, score in data["score"].items()}

        return Tournament(
            data["name"], 
            data["place"], 
            data["note"], 
            datetime.fromisoformat(data["start_date"]) if data["start_date"] else None, 
            datetime.fromisoformat(data["end_date"]) if data["end_date"] else None, 
            rounds, 
            players,
            score            
        )

    def __str__(self):
        return f"Le tournoi {self.name}, se déroulera à {self.place}, remarques : {self.note}"

    def __repr__(self):
        return (
            f"Tournoi( name: {self.name}, place : {self.place}, start_date : {self.start_date},"
            f" end_date : {self.end_date}, round : {self.round}, note : {self.note})"
        )
