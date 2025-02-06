from echecs.models.player import Player
from echecs.views.general_view import GeneralView
from echecs.views.player_view import PlayerView


class PlayerController:

    @staticmethod
    def main_player(store, route_params=None):
        choice = PlayerView.display_home_player(store.players.get_players())

        if choice == 1:
            next = "add_player"
        elif choice == 2:
            next = "homepage"

        return next, None

    @staticmethod
    def add_player(store, route_params=None):
        data = PlayerView.prompt_for_add_player()

        player = Player(**data)
        store.players.add_player(player)

        GeneralView.display_success_message("joueur")
        return "home_player", None
