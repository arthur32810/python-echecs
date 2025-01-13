from echecs.views.player_view import PlayerView


class PlayerController:

    @staticmethod
    def main_player(store=None, input=None):
        choice = PlayerView.display_home_player()

        if choice == "1":
            next = "add_player"
        elif choice == "2":
            next = "list_player"
        elif choice == "3":
            next = "homepage"

        return next, None
