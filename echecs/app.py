from echecs.controllers.home_controller import HomeController
from echecs.controllers.player_controller import PlayerController
from echecs.models.store import Store

import subprocess as sp


class Application:

    routes = {
        "homepage": HomeController.main_menu,
        "home_player": PlayerController.main_player,
        "list_player": PlayerController.list_player,
        "add_player": PlayerController.add_player,
    }

    def __init__(self) -> None:
        self.route = "homepage"
        self.exit = False
        self.route_params = None
        self.store = Store()

    def run(self):
        while not self.exit:

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
