from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView


class PlayerView:

    @staticmethod
    def display_alphabetic_players(players):
        players = sorted(players, key=lambda player: player.last_name)
        PlayerView.list_player(players)

    @staticmethod
    def list_player(players):

        if not players:
            print("\nAucun joueur enregistré \n")
        else:

            # Calculer la largeur maximale pour chaque colonne
            id_width = max(len(player.player_id) for player in players) + 5
            last_name_width = max(len(player.last_name) for player in players) + 5
            first_name_width = max(len(player.first_name) for player in players) + 5
            birthday_width = max(len(player.birthday) for player in players) + 5

            # Ajouter un peu d'espace supplémentaire pour les en-têtes
            id_width = max(id_width, len("ID"))
            last_name_width = max(last_name_width, len("Nom"))
            first_name_width = max(first_name_width, len("Prénom"))
            birthday_width = max(birthday_width, len("Date de naissance"))

            print(
                f"{'ID':<{id_width}} {'Nom':<{last_name_width}} ",
                f"{'Prénom':<{first_name_width}} {'Date de naissance':<{birthday_width}}",
            )

            for player in players:
                print(
                    f"{player.player_id:<{id_width}} {player.last_name.capitalize():<{last_name_width}} ",
                    f"{player.first_name.capitalize():<{first_name_width}} {player.birthday:<{birthday_width}}",
                )

            print("\n------------------------------------")

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
