from echecs.models.tournament import Tournament
from echecs.views.general_view import GeneralView
from echecs.views.tournament_view import TournamentView


class TournamentController:

    @staticmethod
    def main_tournament(store, route_params=None):
        choice = TournamentView.display_home_tournament(store.tournaments.get_tournaments())

        if choice == 1:
            next = "add_tournament"
        elif choice == 2:
            next = "add_round_tournament"
        elif choice == 3:
            next = "list_rapport_tournament"
        elif choice == 4:
            next = "homepage"

        return next, None

    @staticmethod
    def add_tournament(store, route_params=None):
        data = TournamentView.prompt_for_add_tournament()

        tournament = Tournament(**data)
        store.tournaments.add_tournament(tournament)

        GeneralView.display_success_message("tournois")
        return "home_tournament", None
