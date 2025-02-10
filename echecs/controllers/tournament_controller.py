from echecs.models.tournament import Tournament
from echecs.views.choices import Choices
from echecs.views.general_view import GeneralView
from echecs.views.menu_view import MenuView
from echecs.views.tournament_view import TournamentView


class TournamentController:

    @staticmethod
    def main_tournament(store, route_params=None):
        GeneralView.display_header("        GESTION DES TOURNOIS")
        TournamentView.list_tournament(store.tournaments.get_tournaments())

        menu_view = MenuView([Choices.ADD_TOURNAMENT, Choices.DETAIL_TOURNAMENT, Choices.HOME])
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
        selected_tournament = TournamentView.display_select_tournament(store.tournaments.get_tournaments())

        return "detail_tournament", {"id_tournament": selected_tournament}

    @classmethod
    def detail_tournament(cls, store, route_params=None):
        tournament, id_tournament = cls.get_tournament(store, route_params)

        if not tournament:
            return "select_tournament", None

        TournamentView.display_tournament_details(tournament)

        menu_view = MenuView([Choices.ADD_PLAYER_TOURNAMENT, Choices.BACK_HOME_TOURNAMENT])
        menu_view.display()

        return menu_view.selected_choice(), {"id_tournament": id_tournament}

    @classmethod
    def add_player_tournament(cls, store, route_params=None):
        tournament, id_tournament = cls.get_tournament(store, route_params)

        if not tournament:
            return "select_tournament", None

        TournamentView.display_add_player_tournament(tournament, store.players.get_players())

        pass

    def get_tournament(store, route_params=None):
        if not route_params or "id_tournament" not in route_params:
            return False, None

        id_tournament = route_params.get("id_tournament")
        tournament = store.tournaments.get_tournament(id_tournament - 1)

        return tournament, id_tournament
