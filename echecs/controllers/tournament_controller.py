from echecs.views.tournament_view import TournamentView


class TournamentController:

    @staticmethod
    def main_tournament(store, route_params=None):
        choice = TournamentView.display_home_tournament()

        if choice == "1":
            next = "add_tournament"
        elif choice == "2":
            next = "add_round_tournament"
        elif choice == "3":
            next = "list_rapport_tournament"
        elif choice == "4":
            next = "homepage"

        return next, None
