from echecs.models.storePlayer import StorePlayer
from echecs.views.general_view import GeneralView
from echecs.views.player_view import PlayerView


class PlayerController:

    @staticmethod
    def main_player(store, route_params=None):
        choice = PlayerView.display_home_player()

        if choice == "1":
            next = "add_player"
        elif choice == "2":
            next = "list_player"
        elif choice == "3":
            next = "homepage"

        return next, None

    @staticmethod
    def list_player(store, route_params=None):
        PlayerView.display_list_player(store.players.get_players())
        return "home_player", None

    @staticmethod
    def add_player(store, route_params=None):
        first_name, last_name, birthday = PlayerView.prompt_for_add_player()

        store.players.add_player(first_name, last_name, birthday)

        GeneralView.display_success_message("joueur")
        return "home_player", None
