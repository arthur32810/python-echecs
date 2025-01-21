class StoreTournament:

    def __init__(self, save_callback=None):
        self.tournaments = []
        self.save_callback = save_callback

    def add_tournament(self, tournament):
        """Enregistre un tournoi dans le store"""
        self.tournaments.append(tournament)

    def get_tournaments(self):
        return self.tournaments
