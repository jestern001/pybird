# key recorder
from dataclasses import dataclass
from tkinter import Event, Widget


@dataclass
class Keys:
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"


class InputListener:
    def __init__(self, parent: Widget) -> None:
        parent.bind("<KeyPress>", self.set_key)
        parent.bind("<KeyRelease>", self.unset_key)
        self.key_states = {}

    def set_key(self, event: Event):
        self.key_states[event.keysym] = True

    def unset_key(self, event: Event):
        self.key_states[event.keysym] = False