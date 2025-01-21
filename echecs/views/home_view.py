from echecs.views.general_view import GeneralView


class HomeView:

    @staticmethod
    def home():
        GeneralView.display_header("  BIENVENUE DANS LE CENTRE ÉCHECS")
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("4. Quitter le programme")
        print("------------------------------------")

        return GeneralView.choice_enter_menu(4)
