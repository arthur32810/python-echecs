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

        check_date = False
        while check_date is not True:
            start_date = input("Date de debut (JJ/MM/AAAA) : ")
            end_date = input("Date de Fin (JJ/MM/AAAA) : ")

            if (
                (is_valid_date(start_date) and is_date_not_before_today(start_date))
                and (is_valid_date(end_date) and is_date_not_before_today(end_date))
                and is_date_not_before(start_date, end_date)
            ):
                check_date = True
            else:
                check_date = False

        round = InputView.get_integer_input("Nombre de tours (par défaut 4) : ")
        note = input("Remarques (optionnel) : ")

        return {
            "name": name,
            "place": place,
            "start_date": start_date,
            "end_date": end_date,
            "round": round,
            "note": note,
        }
