from echecs.views.choices import Choices
from echecs.models.player import Player
from echecs.views.general_view import GeneralView
from echecs.views.menu_view import MenuView
from echecs.views.player_view import PlayerView


class PlayerController:

    @staticmethod
    def main_player(store, route_params=None):

        GeneralView.display_header("        GESTION DES JOUEURS")
        PlayerView.list_player(store.players.get_players())

        menu_view = MenuView([Choices.ADD_PLAYER, Choices.HOME])
        menu_view.display()

        return menu_view.selected_choice(), None

    @staticmethod
    def add_player(store, route_params=None):
        data = PlayerView.prompt_for_add_player()

        player = Player(**data)
        store.players.add_player(player)

        GeneralView.display_success_message("joueur")
        return "home_player", None
