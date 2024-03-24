# key recorder
from tkinter import Event, Widget


class InputListener:
    def __init__(self, parent: Widget) -> None:
        parent.bind("<KeyPress>", self.set_key)
        parent.bind("<KeyRelease>", self.unset_key)
        self.key_states = {}

    def set_key(self, event: Event):
        self.key_states[event.keysym] = True

    def unset_key(self, event: Event):
        self.key_states[event.keysym] = False