from echecs.models.tournament import Tournament
from echecs.views.choices import Choices
from echecs.views.general_view import GeneralView
from echecs.views.menu_view import MenuView
from echecs.views.round_view import RoundView
from echecs.views.tournament_view import TournamentView
from echecs.models.constant import TOURNAMENT_ROUNDS
from datetime import datetime


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

        if tournament.rounds:
            return "tournament_rounds", {"id_tournament": id_tournament}

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

        # Affiche les détails du tournoi
        TournamentView.display_tournament_details(tournament)

        # Si le tournoi n'a pas de rounds, on commence le tournoi
        if len(tournament.rounds) == 0:
            tournament.start_tournament()

        # On affiche chaque rounds passés
        for round in tournament.rounds:

            RoundView.display_round(round)

        if tournament.end_date:
            RoundView.prompt_end_tournament()
            return "home_tournament", None

        if not tournament.end_date:

            # On Récupére le dernier round pour afficher la saisie des résultats
            last_round = tournament.rounds[-1]

            if not last_round.is_finished:
                RoundView.display_select_result_round(last_round)
                route, match = RoundView.prompt_for_round_result(last_round)

                if route != "select_winner":
                    return route, {"id_tournament": id_tournament}

                # On demande de choisir qui a gagné le match
                winner = RoundView.prompt_select_winner(match)
                match winner:
                    case 1:
                        match.player1_win()
                        tournament.score[match.player1] += 1
                    case 2:
                        match.player2_win()
                        tournament.score[match.player2] += 1
                    case 3:
                        match.match_nul()
                        tournament.score[match.player1] += 0.5
                        tournament.score[match.player2] += 0.5
                    case _:
                        return "tournament_rounds", {"id_tournament": id_tournament}
                    
                #On défini l'heure de début du round
                if not last_round.start_time:
                    last_round.start_time = datetime.now()
                elif last_round.is_finished and not last_round.end_time:
                    last_round.end_time = datetime.now()
                else:
                    None
            
            elif last_round.is_finished and len(tournament.rounds) < TOURNAMENT_ROUNDS:
                tournament.next_round()
            
            elif last_round.is_finished and len(tournament.rounds) == TOURNAMENT_ROUNDS and not tournament.end_date:
                tournament.end_tournament()
            
            else:
                None

            return "tournament_rounds", {"id_tournament": id_tournament}
        else:

