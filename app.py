from inputlistener import InputListener
from room import Room

from pathlib import Path
from tkinter import Canvas, Tk


class App:
    def __init__(self, grid_size: int, room_speed: float, move_speed: float) -> None:
        self._tk = Tk()
        self.input = InputListener(self._tk)
        self._tk.after(room_speed, self._game_loop)
        self.room = Room(self._tk, Path(r"configs\rooms\start.json"), grid_size, self.input, move_speed)
        
        # settings
        self.grid_size = grid_size
        self.room_speed = room_speed
        self.move_speed = move_speed

    def _game_loop(self):
        self.room.update()
        self.room.after(self.room_speed, self._game_loop)

    def start(self):
        self._tk.mainloop()