from echecs.utils.date_validator import (
    is_date_not_before,
    is_date_not_before_today,
    is_valid_date,
)
from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView


class TournamentView:

    @staticmethod
    def display_home_tournament():
        GeneralView.display_header("        GESTION DES TOURNOIS")

        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des tours à un tournoi existant")
        print("3. Afficher les rapports d’un tournoi")
        print("\n4. Retour au menu principal")

        print("------------------------------------")
        return InputView.choice_enter_menu(4)

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
