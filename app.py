from pathlib import Path
from colors import Colors
from gamesettings import GameSettings
from inputlistener import InputListener
from room import Room


from tkinter import Canvas, Tk


class App:
    def __init__(
        self,
        config_dir: Path
    ) -> None:
        # get config
        self.game_settings = GameSettings(config_dir)

        # set game settings from config
        self.update_rate = self.game_settings.game_config.update_rate

        # set tk
        self.tk = Tk()
        self.canvas = Canvas(self.tk, bg=Colors.GREEN)
        self.canvas.pack()

        # set up game
        self.input_listener = InputListener(self.tk)
        start_room_name = self.game_settings.game_config.start_room_name
        self.room = Room(
            canvas=self.canvas,
            input_listener=self.input_listener,
            room_settings=self.game_settings.get_room_settings(room_name=start_room_name)
        )

        # set up game loop
        self.game_loop()

    def game_loop(self):
        self.room.update()
        self.tk.after(self.update_rate, self.game_loop)

    def run(self):
        self.tk.mainloop()
