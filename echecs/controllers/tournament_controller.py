from echecs.models.tournament import Tournament
from echecs.views.choices import Choices
from echecs.views.general_view import GeneralView
from echecs.views.menu_view import MenuView
from echecs.views.round_view import RoundView
from echecs.views.tournament_view import TournamentView
from echecs.models.constants import TOURNAMENT_ROUNDS


class TournamentController:

    @staticmethod
    def main_tournament(store, route_params=None):
        GeneralView.display_header("        GESTION DES TOURNOIS")
        TournamentView.list_tournament(store.tournaments.get_tournaments())

        menu_view = MenuView(Choices.ADD_TOURNAMENT, Choices.DETAIL_TOURNAMENT, Choices.HOME)
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

        menu_view = None

        if not tournament.players:
            menu_view = MenuView(Choices.ADD_PLAYER_TOURNAMENT, Choices.BACK_HOME_TOURNAMENT)

        elif tournament.players:
            menu_view = MenuView(Choices.TOURNAMENT_ROUND, Choices.BACK_HOME_TOURNAMENT)

        menu_view.display()
        return menu_view.selected_choice(), {"id_tournament": id_tournament}

    @classmethod
    def add_player_tournament(cls, store, route_params=None):
        tournament, id_tournament = cls.get_tournament(store, route_params)

        if not tournament:
            return "select_tournament", None

        player_selected = TournamentView.display_add_player_tournament(tournament, store.players.get_players())

        store.tournaments.add_players_tournament(id_tournament=id_tournament, players=player_selected)

        TournamentView.display_message_player_added()
        return "detail_tournament", {"id_tournament": id_tournament}

    def get_tournament(store, route_params=None):
        if not route_params or "id_tournament" not in route_params:
            return False, None

        id_tournament = route_params.get("id_tournament")
        tournament = store.tournaments.get_tournament(id_tournament)

        return tournament, id_tournament

    @classmethod
    def tournament_rounds(cls, store, route_params=None):
        tournament, id_tournament = cls.get_tournament(store, route_params)

        if not tournament:
            return "select_tournament", None

        TournamentView.display_tournament_details(tournament)

        if len(tournament.rounds) == 0:
            tournament.start_tournament()

            RoundView.display_round(tournament.rounds[0])

        # while True:
        #     numero_rounds = len(tournament.rounds)

        #     if numero_rounds == 0:
        #         tournament.start_tournament()

        #     if numero_rounds == TOURNAMENT_ROUNDS - 1 and tournament.rounds[TOURNAMENT_ROUNDS - 1].completed:
        #         GeneralView.display_error_message("Le tournoi est terminé")
        #         return "detail_tournament", {"id_tournament": id_tournament}

        #     if tournament.rounds[numero_rounds - 1].completed:
        #         tournament.start_round()

        #     round = tournament.rounds[numero_rounds - 1]

        #     TournamentView.display_round_details(round)
