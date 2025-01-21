from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView


class TournamentView:

    @staticmethod
    def display_home_tournament():
        GeneralView.display_header("        GESTION DES TOURNOIS")

        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des tours à un tournoi existant")
        print("3. Afficher les rapports d’un tournoi")
        print("4. Retour au menu principal")

        print("------------------------------------")
        return InputView.choice_enter_menu(4)

    @staticmethod
    def prompt_for_add_tournament():
        GeneralView.display_header("        CRÉER UN NOUVEAU TOURNOI")

        name = input("Nom du tournoi : ")
        place = input("Lieu : ")
        start_date = InputView.get_date_input("Date de debut (JJ/MM/AAAA) : ")
        end_date = InputView.get_date_input("Date de Fin (JJ/MM/AAAA) : ")
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
