
from tkinter import Tk


BASE_SIZE = 16
WINDOW_HEIGHT = 240
WINDOW_WIDTH = 256


class Game(Tk):

    def run(
        self, 
        window_height: int = WINDOW_HEIGHT, 
        window_width: int = WINDOW_WIDTH
    ):
        self.geometry(f"{window_width}x{window_height}")
        self.mainloop()


if __name__ == "__main__":
    game = Game()
    game.run()