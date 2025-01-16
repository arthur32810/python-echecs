from echecs.utils.date_validator import is_valid_date
from echecs.utils.player_identifiant_validator import is_valid_player_identifiant
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
    def display_list_player(players):
        GeneralView.display_header("   LISTE DES JOUEURS (ALPHABÉTIQUE)")

        if not players:
            print("\nAucun joueur enregistré")
        else:
            print("ID\tNom\tPrénom\tDate de naissance")

        for player in players:
            print(
                f"{player.id}\t{player.last_name}\t{player.first_name}\t{player.birthday}"
            )

        print("\n------------------------------------")
        input("Appuyez sur Entrée pour retourner au menu précédent...")

    @staticmethod
    def prompt_for_add_player():
        GeneralView.display_header("       AJOUTER UN NOUVEAU JOUEUR")

        first_name = input("Prénom : ")
        last_name = input("Nom : ")

        birthday = input("Date de naissance (JJ/MM/AAAA) : ")
        while is_valid_date(birthday) is not True:
            print(
                "Erreur dans la date de naissance, veuillez saisir une date au format JJ/MM/AAAA"
            )
            birthday = input("Date de naissance (JJ/MM/AAAA) : ")

        player_id = input("Identifiant nationnal d'éches : ")
        while is_valid_player_identifiant(player_id) is not True:
            print(
                "Erreur dans le format de l'identifiant. Voilà le format attendu : deux lettres et cinq chiffres (ex: AB12345)"
            )
            player_id = input("Identifiant nationnal d'éches : ")

        print("\n------------------------------------")

        return {
            "id": player_id,
            "first_name": first_name,
            "last_name": last_name,
            "birthday": birthday,
        }
