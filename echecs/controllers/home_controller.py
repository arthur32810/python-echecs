from echecs.views.choices import Choices
from echecs.views.general_view import GeneralView
from echecs.views.home_view import HomeView
from echecs.views.menu_view import MenuView


class HomeController:

    @staticmethod
    def main_menu(store=None, route_params=None):

        GeneralView.display_header("  BIENVENUE DANS LE CENTRE ÉCHECS")

        menu_view = MenuView(Choices.HOME_PLAYER, Choices.HOME_TOURNAMENT)
        menu_view.display()

        return menu_view.selected_choice(), None

    @staticmethod
    def exit(store=None, route_params=None):
        HomeView.exit()
