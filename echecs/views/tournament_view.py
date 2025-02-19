from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView
from echecs.views.player_view import PlayerView


class TournamentView:

    @staticmethod
    def display_home_tournament(tournaments):

        print("\n1. Créer un nouveau tournoi")
        print("2. Voir les détails d'un tournoi")
        print("\n3. Retour au menu principal")

        print("------------------------------------")
        return InputView.choice_enter_menu(4)

    @staticmethod
    def list_tournament(tournaments):
        name_width = max(len(tournament.name) for tournament in tournaments) + 5
        place_width = max(len(tournament.place) for tournament in tournaments) + 5

        name_width = max(name_width, len("Nom"))
        place_width = max(place_width, len("Lieu"))

        if not tournaments:
            print("\nAucun tournoi enregistré")
        else:
            print(f"ID {'Nom':<{name_width}} {'Lieu':<{place_width}}")

            for index, tournament in enumerate(tournaments):
                print(f"{index+1:<2} {tournament.name:<{name_width}} {tournament.place:<{place_width}}")

            print("\n------------------------------------")

    @staticmethod
    def prompt_for_add_tournament():
        GeneralView.display_header("        CRÉER UN NOUVEAU TOURNOI")

        name = InputView.get_required_input("Nom du tournoi : ")
        place = InputView.get_required_input("Lieu : ")
        note = input("Remarques (optionnel) : ")

        print("\n------------------------------------")

        return {
            "name": name,
            "place": place,
            "note": note,
        }

    @staticmethod
    def display_select_tournament(tournaments):
        GeneralView.display_header("      SÉLECTIONNER UN TOURNOI")

        TournamentView.list_tournament(tournaments)

        id_tournament = InputView.selected_choice(
            f"Sélectionner un tournoi (1-{len(tournaments)}): ", len(tournaments)
        )

        return id_tournament - 1

    @staticmethod
    def display_tournament_details(tournament):
        GeneralView.display_header("      DÉTAILS DU TOURNOI")

        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Remarques : {tournament.note}")

        if not tournament.players:
            print("\nJoueurs : Aucun joueur inscrit")

        if tournament.players:
            print("\nJoueurs :")
            # for player in tournament.players:
            #     print(f" - {player.first_name} {player.last_name}")
            print(tournament.players)

        print("\n------------------------------------")

    @staticmethod
    def display_add_player_tournament(tournament, list_store_players):

        GeneralView.display_header("      AJOUTER UN JOUEUR AU TOURNOI")

        print(f"Nom : {tournament.name}")
        print(f"Lieu : {tournament.place}")
        print(f"Remarques : {tournament.note}")

        print("\nSélectionner les joueurs à ajouter au tournoi : \n")

        PlayerView.list_player(list_store_players)
