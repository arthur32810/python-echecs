from echecs.models.tournament import Tournament


class StoreTournament:

    def __init__(self):
        self.tournaments = []

    def add_tournament(self, tournament):
        """Enregistre un tournoi dans le store"""
        self.tournaments.append(tournament)

    def add_players_tournament(self, id_tournament, players):
        """Ajoute un joueur à un tournoi"""
        tournament = self.get_tournament(id_tournament)
        tournament.players = players

    def get_tournaments(self):
        return self.tournaments

    def get_tournament(self, index):
        if index <= len(self.tournaments):
            return self.tournaments[index]
        else:
            return None

    def to_dict(self):
        return [tournament.to_dict() for tournament in self.tournaments]

    def from_dict(self, data, store):
        self.tournaments = [Tournament.from_dict(tournament, store) for tournament in data]
