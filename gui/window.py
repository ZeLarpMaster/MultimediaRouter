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
        self.init_widgets()

    def init_widgets(self):
        self.bucket_frame = BucketList(self.master, self.on_bucket_update, self.app.list_buckets())
        self.routes_frame = RouteList(self.master, self.on_route_update, self.app.list_routes())

    def on_bucket_update(self):
        self.app.set_buckets(self.bucket_frame.get_buckets())

    def on_route_update(self):
        self.app.set_routes(self.routes_frame.get_routes())
