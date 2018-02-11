import os
import time

from tkinter import *
from tkinter.filedialog import askdirectory


class RouteList(LabelFrame):
    def __init__(self, master, on_update, initial_routes):
        super().__init__(master, text="Routes")
        self.pack(fill=X, ipadx=16, ipady=16)
        self.routes = {}
        self.frames = {}
        self.on_update = on_update
        self.init_widgets(initial_routes)

    def init_widgets(self, initial_routes):
        button_bar = Frame(self)
        button_bar.pack(side=TOP, ipadx=16)
        Button(button_bar, text="+", command=self.generate_frame).pack(side=LEFT)
        for ext, route in initial_routes.items():
            self.generate_frame(ext, route)

    def get_routes(self):
        return {ext.get(): route.get() for ext, route in self.routes.values()}

    def ask_dir(self, var: StringVar):
        def result():
            directory = askdirectory(title="Choississez un répertoire", initialdir=os.getcwd())
            if len(directory) > 0:
                var.set(directory)
        return result

    def raw_update(self, *_):
        if self.on_update is not None:
            self.on_update()

    def delete_frame(self, uuid: str):
        def result():
            frame = self.frames.pop(uuid)
            frame.destroy()
            self.routes.pop(uuid)
            self.raw_update(uuid)
        return result

    def generate_frame(self, preset_extension: str="", preset_route: str=""):
        uuid = str(hash(time.clock()))
        frame = Frame(self)
        frame.pack(expand=True, fill=X)
        ext_var = StringVar(name=uuid+"ext", value=preset_extension)
        ext_var.trace_add("write", self.raw_update)
        route_var = StringVar(name=uuid+"rte", value=preset_route)
        route_var.trace_add("write", self.raw_update)
        Button(frame, text="-", command=self.delete_frame(uuid)).pack(side=LEFT)
        Entry(frame, textvariable=ext_var).pack(side=LEFT)
        Entry(frame, textvariable=route_var, state="readonly").pack(side=LEFT, expand=True, fill=X)
        Button(frame, text="...", command=self.ask_dir(route_var)).pack(side=LEFT)
        self.frames[uuid] = frame
        self.routes[uuid] = (ext_var, route_var)
