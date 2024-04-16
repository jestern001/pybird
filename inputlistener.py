# key recorder
from tkinter import Event, Tk


@dataclass
class Keys:
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"


class InputListener:
    def __init__(self, parent: Tk) -> None:
        parent.bind("<KeyPress>", self.set_key)
        parent.bind("<KeyRelease>", self.unset_key)
        self.key_pressed = {}

    def set_key(self, event: Event):
        self.key_pressed[event.keysym] = True

    def unset_key(self, event: Event):
        self.key_pressed[event.keysym] = False
