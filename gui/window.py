import threading
import ctypes

from tkinter.ttk import Progressbar
from tkinter import messagebox
from tkinter import *

from core import App
from .buckets import BucketList
from .routes import RouteList


class Window(Frame):
    def __init__(self, app: App, master):
        super().__init__(master)
        self.pack()
        self.app = app
        self.master.title("Multimedia File Router")
        self.master.minsize(500, 200)
        self.master.option_add("*tearOff", False)
        self.progress_current = Variable(name="progress_current", value=0.0)
        self.copy_enabled = StringVar(value=self.app.get_copy())
        self.init_widgets()

    def init_widgets(self):
        self.init_menu()
        self.bucket_frame = BucketList(self.master, self.on_bucket_update, self.app.list_buckets())
        self.routes_frame = RouteList(self.master, self.on_route_update, self.app.list_routes())

    def init_menu(self):
        self.menu_bar = Menu(self.master)
        self.master["menu"] = self.menu_bar
        self.init_tools_menu()
        self.init_config_menu()

    def init_config_menu(self):
        self.menu_config = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_config, label="Options")

        self.menu_config.add_checkbutton(label="Créer des copies", variable=self.copy_enabled, onvalue=1, offvalue=0,
                                         command=self.update_copy)

    def init_tools_menu(self):
        self.menu_tools = Menu(self.menu_bar)
        self.menu_bar.add_cascade(menu=self.menu_tools, label="Outils")

        self.menu_tools.add_command(label="Exécuter", command=self.execute)

    def update_copy(self):
        self.app.set_copy(self.copy_enabled.get() == "1")

    def execute(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 0 and self.copy_enabled.get() == "0":
            messagebox.showerror("Impossible d'exécuter", "Vous devez exécuter le programme en tant qu'administrateur "
                                                          "pour créer des liens vers les fichiers.")
        else:
            self.thread = threading.Thread(target=self.app.run, args=(self.on_progress,), daemon=True)
            self.thread.start()

    def cleanup_thread(self):
        self.thread = None

    def on_progress(self, current: int, total: int, done: bool):
        if done is True:
            self.master.after(0, func=self.cleanup_thread)
            self.progress_bar.destroy()
            self.menu_tools.entryconfig("Exécuter", state="normal")
        elif current is not None and total is not None:
            self.progress_bar.stop()
            self.progress_bar["maximum"] = total
            self.progress_bar["mode"] = "determinate"
            self.progress_current.set(value=current)
        else:
            self.progress_bar = Progressbar(self.master, mode="indeterminate", variable=self.progress_current)
            self.progress_bar.start()
            self.progress_bar.pack(side=BOTTOM, fill=X, expand=True)
            self.menu_tools.entryconfig("Exécuter", state="disabled")
        self.master.update()

    def on_bucket_update(self):
        self.app.set_buckets(self.bucket_frame.get_buckets())

    def on_route_update(self):
        self.app.set_routes(self.routes_frame.get_routes())
