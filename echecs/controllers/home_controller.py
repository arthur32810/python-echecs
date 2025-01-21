from echecs.views.home_view import HomeView


class HomeController:

    @staticmethod
    def main_menu(store=None, route_params=None):
        choice = HomeView.home()

        if choice == 1:
            next = "home_player"
        elif choice == 2:
            next = "home_tournament"
        elif choice == 3:
            next = "quit"

        return next, None

    @staticmethod
    def exit(store=None, route_params=None):
        HomeView.exit()
