from echecs.views.general_view import GeneralView


class PlayerView:

    @staticmethod
    def display_home_player():
        GeneralView.display_header("        GESTION DES JOUEURS")
        print("1. Ajouter un joueur")
        print("2. Afficher la liste des joueurs")
        print("3. Retour au menu principal")
        print("------------------------------------")
        return input("Veuillez selectionner une option (1-3) : ")

    @staticmethod
    def display_players(players):
        GeneralView.display_header("   LISTE DES JOUEURS (ALPHABÉTIQUE)")

        if not players:
            print("Aucun joueur enregistré")

        for index, player in enumerate(players):
            print(f"{index+1}. {player.last_name}, {player.first_name}")

    @staticmethod
    def prompt_for_add_player():
        GeneralView.display_header("       AJOUTER UN NOUVEAU JOUEUR")
