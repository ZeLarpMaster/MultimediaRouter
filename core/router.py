import os
import os.path
import shutil

from core import CATEGORIES


class Router:
    def __init__(self, routes: dict, *, verbose: bool=False, copy: bool=False):
        self.routes = routes
        self.verbose = verbose
        self.should_copy = copy

    def update_copy(self, value: bool):
        self.should_copy = value

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
            if not self.should_copy:
                self.log("Création du lien symbolique: {}".format(destination))
                os.symlink(filepath, destination)
            else:
                self.log("Copie du fichier: {}".format(destination))
                shutil.copy2(filepath, destination)

    def log(self, message):
        if self.verbose:
            print(message)
