import json
import os
import os.path
import glob
import typing

from core import Router


class App:
    def __init__(self, config_path: os.PathLike, *, verbose: bool=False):
        self.verbose = verbose
        self.config_path = config_path
        self.load_config()
        self.router = Router(self.configs["routes"],
                             verbose=verbose,
                             copy=self.configs.get("should_copy", False))

    def run(self, callback: typing.Callable[[int, int], None]=None):
        callback(None, None, False)
        all_paths = []
        for bucket in self.configs["buckets"]:
            self.log("Ajout en cache des fichiers du seau: {}".format(bucket))
            all_paths.extend(glob.iglob(os.path.join(bucket, "**", "*"), recursive=True))
        length = len(all_paths)
        callback(0, length, False)
        for i, path in enumerate(all_paths):
            self.router.handle(path)
            if callback is not None:
                callback(i+1, length, False)
        callback(length, length, True)

    def get_copy(self) -> bool:
        return self.configs.get("should_copy", False)

    def set_copy(self, value: bool):
        self.configs["should_copy"] = value
        self.router.update_copy(value)

    def set_buckets(self, buckets: typing.List[os.PathLike]):
        self.configs["buckets"].clear()
        self.configs["buckets"].extend(buckets)
        self.save_config()

    def add_bucket(self, filepath: os.PathLike):
        self.configs["buckets"].append(filepath)
        self.save_config()

    def remove_bucket(self, filepath: os.PathLike):
        self.configs["buckets"].remove(filepath)
        self.save_config()

    def list_buckets(self):
        return self.configs["buckets"].copy()

    def add_route(self, extension: str, destination: os.PathLike):
        self.configs["routes"][extension] = os.path.normpath(destination)
        self.router.update_routes(self.configs["routes"])
        self.save_config()

    def remove_route(self, extension: str):
        self.configs["routes"].pop(extension, None)
        self.router.update_routes(self.configs["routes"])
        self.save_config()

    def set_routes(self, routes: typing.Dict[str, os.PathLike]):
        self.configs["routes"].clear()
        self.configs["routes"].update(routes)
        self.save_config()

    def list_routes(self):
        return self.configs["routes"].copy()

    def save_config(self):
        self.log("Mise à jour du fichier de configuration ({}).".format(self.config_path))
        with open(self.config_path, "w") as fp:
            json.dump(self.configs, fp, indent=4)

    def load_config(self):
        if not os.path.exists(self.config_path):
            self.log("Création du fichier de configuration par défaut.")
            with open(self.config_path, "w") as fp:
                json.dump({"routes": {}, "buckets": []}, fp)
        self.log("Chargement du fichier de configuration ({}).".format(self.config_path))
        with open(self.config_path, "r") as fp:
            self.configs = json.load(fp)

    def log(self, message):
        if self.verbose:
            print(message)
