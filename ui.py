from core import App
from gui import Window
from tkinter import Tk


def main():
    app = App("config.json")
    root = Tk()
    window = Window(app, root)
    window.mainloop()

if __name__ == "__main__":
    main()
