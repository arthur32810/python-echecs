from echecs.models.tournament import Tournament


class StoreTournament:

    def __init__(self, save_callback=None):
        self.tournaments = []
        self.save_callback = save_callback

    def add_tournament(self, tournament):
        """Enregistre un tournoi dans le store"""
        self.tournaments.append(tournament)

        if self.save_callback:
            self.save_callback()

    def get_tournaments(self):
        return self.tournaments

    def to_dict(self):
        return [tournament.to_dict() for tournament in self.tournaments]

    def from_dict(self, data):
        self.tournaments = [Tournament.from_dict(tournament) for tournament in data]
