from echecs.models.constant import TOURNAMENT_PLAYERS
from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView
from echecs.views.player_view import PlayerView
from echecs.views.round_view import RoundView


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

        if not tournaments:
            print("\nAucun tournoi enregistré \n")
        else:
            name_width = max(len(tournament.name) for tournament in tournaments) + 5
            place_width = max(len(tournament.place) for tournament in tournaments) + 5

            name_width = max(name_width, len("Nom"))
            place_width = max(place_width, len("Lieu"))

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
        print(f"Date de début : {tournament.start_date.strftime("%d/%m/%Y %H:%M")}") if tournament.start_date else None
        print(f"Date de fin : {tournament.end_date.strftime("%d/%m/%Y %H:%M")}") if tournament.end_date else None

        if not tournament.players:
            print("\nJoueurs : Aucun joueur inscrit \n")

        if tournament.players:
            print("\nJoueurs : \n")
            PlayerView.list_player(tournament.players)

        # On affiche chaque rounds passés
        for round in tournament.rounds:
            RoundView.display_round(round)

    def display_add_player_tournament(tournament, list_store_players):

        print("\nSélectionner les joueurs à ajouter au tournoi : \n")

        PlayerView.list_player(list_store_players)

        player_selected = []

        while len(player_selected) < TOURNAMENT_PLAYERS:
            id_player_choice = input(f"Rentrer l'id du joueur {len(player_selected)+1} :")

            player_choice = next(
                (player for player in list_store_players if player.player_id == id_player_choice), None
            )

            if not player_choice:
                print("Ce joueur n'existe pas")

            elif player_choice in player_selected:
                print("Ce joueur est déjà sélectionné")

            elif player_choice:
                player_selected.append(player_choice)
                print(f"Le joueur {player_choice} a bien été ajouté")

        return player_selected

    def display_message_player_added():
        print(f"\nLes {TOURNAMENT_PLAYERS} joueurs ont été ajoutés au tournoi")

    @staticmethod
    def display_classement(classement):

        print("\nClassement :")

        for index, player in enumerate(classement):
            print(f"\t{index+1}. {player[0]} - {player[1]} points")

        print("\n------------------------------------")
