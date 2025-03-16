import subprocess as sp
import pdb

from echecs.controllers.home_controller import HomeController
from echecs.controllers.player_controller import PlayerController
from echecs.controllers.tournament_controller import TournamentController
from echecs.models.store import Store


class Application:

    routes = {
        "homepage": HomeController.main_menu,
        # players
        "home_player": PlayerController.main_player,
        "add_player": PlayerController.add_player,
        # tournaments
        "home_tournament": TournamentController.main_tournament,
        "add_tournament": TournamentController.add_tournament,
        "select_tournament": TournamentController.select_tournament,
        "detail_tournament": TournamentController.detail_tournament,
        "add_player_tournament": TournamentController.add_player_tournament,
        "tournament_rounds": TournamentController.tournament_rounds,
        "start_round": TournamentController.start_round,
        "end_tournament": TournamentController.end_tournament,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        try:
            while not self.exit:
                try:

                    # Clear the shell output
                    sp.call("clear", shell=True)

                    # Get the controller method with routes array
                    controller_method = self.routes[self.route]

                    # Call the controller method, we pass the store and the route's
                    # parameters.
                    # Every controller should return two things:
                    # - the next route to display
                    # - the parameters needed for the next route
                    next_route, next_params = controller_method(self.store, self.route_params)

                    # set the next route and input
                    self.route = next_route
                    self.route_params = next_params

                    # if the controller returned "quit" then we end the loop
                    if next_route == "quit":
                        self.exit = True
                except KeyboardInterrupt:
                    self.exit = True

            # Clear the shell output
            sp.call("clear", shell=True)
            HomeController.exit()

        except Exception as e:
            print(f"Une erreur est survenue : {e}")
            pdb.post_mortem()
