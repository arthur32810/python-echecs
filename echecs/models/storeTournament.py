from echecs.models.tournament import Tournament


class StoreTournament:

    def __init__(self, save_callback=None):
        self.tournaments = []
        self.save_callback = save_callback
