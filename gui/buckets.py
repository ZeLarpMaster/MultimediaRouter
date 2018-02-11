import os
import time

from tkinter import *
from tkinter.filedialog import askdirectory


class BucketList(LabelFrame):
    def __init__(self, master, on_update, initial_buckets):
        super().__init__(master, text="Seaux")
        self.pack(fill=X, ipadx=16, ipady=16)
        self.buckets = {}
        self.frames = {}
        self.on_update = on_update
        self.init_widgets(initial_buckets)

    def init_widgets(self, initial_buckets):
        button_bar = Frame(self)
        button_bar.pack(side=TOP, ipadx=16)
        Button(button_bar, text="+", command=self.generate_frame).pack(side=LEFT)
        for bucket in initial_buckets:
            self.generate_frame(bucket)

    def get_buckets(self):
        return [b.get() for b in self.buckets.values()]

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
            self.buckets.pop(uuid)
            self.raw_update(uuid)
        return result

    def generate_frame(self, preset_value: str=""):
        uuid = str(hash(time.clock()))
        frame = Frame(self)
        frame.pack(expand=True, fill=X)
        var = StringVar(name=uuid, value=preset_value)
        var.trace_add("write", self.raw_update)
        Button(frame, text="-", command=self.delete_frame(uuid)).pack(side=LEFT)
        Entry(frame, textvariable=var, state="readonly").pack(side=LEFT, expand=True, fill=X)
        Button(frame, text="...", command=self.ask_dir(var)).pack(side=LEFT)
        self.frames[uuid] = frame
        self.buckets[uuid] = var
