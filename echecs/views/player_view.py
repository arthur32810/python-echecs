from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView


class PlayerView:

    @staticmethod
    def display_home_player():
        GeneralView.display_header("        GESTION DES JOUEURS")
        print("1. Ajouter un joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Retour au menu principal")
        print("------------------------------------")
        return InputView.choice_enter_menu(3)

    @staticmethod
    def display_list_player(players):
        GeneralView.display_header("   LISTE DES JOUEURS (ALPHABÉTIQUE)")

        if not players:
            print("\nAucun joueur enregistré")
        else:
            print("ID\tNom\tPrénom\tDate de naissance")

        for player in players:
            print(f"{player.player_id}\t{player.last_name}\t{player.first_name}\t{player.birthday}")

        print("\n------------------------------------")
        input("Appuyez sur Entrée pour retourner au menu précédent...")

    @staticmethod
    def prompt_for_add_player():
        GeneralView.display_header("       AJOUTER UN NOUVEAU JOUEUR")

        first_name = InputView.get_required_input("Prénom : ")
        last_name = InputView.get_required_input("Nom : ")

        birthday = InputView.get_birthday_input()

        player_id = InputView.get_player_id_input()

        print("\n------------------------------------")

        return {
            "player_id": player_id,
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
        }
