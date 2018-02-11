import argparse
import ctypes

from core import App


def main():
    parser = argparse.ArgumentParser(description="Exécuter le routeur multimédia")
    parser.add_argument("config", type=argparse.FileType(), help="le fichier de configuration du routeur")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, dest="v",
                        help="ajoute des messages verboses pendant l'exécution")
    args = parser.parse_args()
    args.config.buffer.close()
    app = App(args.config.name, verbose=args.v)
    app.run()

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        print("Cette application nécessite les droits d'administrateur pour s'exécuter correctement.")
    else:
        main()
