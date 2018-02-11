import os
import os.path

from core import CATEGORIES


class Router:
    def __init__(self, routes: dict, *, verbose: bool=False):
        self.routes = routes
        self.verbose = verbose

    def update_routes(self, new_routes):
        self.routes = new_routes

    def get_route(self, extension):
        return self.routes.get(extension, self.routes.get(CATEGORIES.get(extension)))

    def get_file_destination(self, filename: str) -> os.PathLike:
        extension = os.path.splitext(filename)[-1]
        route = self.get_route(extension)
        return route and os.path.join(route, filename)

    def handle(self, filepath: os.PathLike):
        filename = os.path.basename(filepath)
        destination = self.get_file_destination(filename)
        if destination and not os.path.exists(destination):
            self.log("Création du lien symbolique: {}".format(destination))
            os.symlink(filepath, destination)

    def log(self, message):
        if self.verbose:
            print(message)
