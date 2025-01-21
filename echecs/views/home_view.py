from echecs.views.general_view import GeneralView
from echecs.views.input_view import InputView


class HomeView:

    @staticmethod
    def home():
        GeneralView.display_header("  BIENVENUE DANS LE CENTRE ÉCHECS")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("\n3. Quitter le programme")
        print("------------------------------------")

        return InputView.choice_enter_menu(3)

    @staticmethod
    def exit():
        GeneralView.display_header("MERCI D’AVOIR UTILISÉ L’APPLICATION")
