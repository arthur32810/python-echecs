from echecs.models.tournament import Tournament
from echecs.views.general_view import GeneralView
from echecs.views.tournament_view import TournamentView
from echecs.views.menu_view import MenuView
from echecs.views.choices import Choices


class TournamentController:

    @staticmethod
    def main_tournament(store, route_params=None):
        GeneralView.display_header("        GESTION DES TOURNOIS")
        TournamentView.list_tournament(store.tournaments.get_tournaments())

        menu_view = MenuView([Choices.ADD_TOURNAMENT, Choices.SELECT_TOURNAMENT, Choices.HOME])
        menu_view.display()

        return menu_view.selected_choice(), None

    @staticmethod
    def add_tournament(store, route_params=None):
        data = TournamentView.prompt_for_add_tournament()

        tournament = Tournament(**data)
        store.tournaments.add_tournament(tournament)

        GeneralView.display_success_message("tournois")
        return "home_tournament", None

    @staticmethod
    def select_tournament(store, route_params=None):
        choice = TournamentView.display_select_tournament(store.tournaments.get_tournaments())

        print("choix : ", choice)
