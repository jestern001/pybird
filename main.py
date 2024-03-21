from tkinter import Canvas, Tk

from colors import Colors


BASE_SIZE = 16
WINDOW_HEIGHT = 240
WINDOW_WIDTH = 256


class Window(Tk):

    def run(
        self, 
        window_height: int = WINDOW_HEIGHT, 
        window_width: int = WINDOW_WIDTH
    ):

        # add a view
        view = Canvas(self, bg=Colors.RED)
        view.pack()

        # run
        self.geometry(f"{window_width}x{window_height}")
        self.mainloop()


if __name__ == "__main__":
    game = Window()
    game.run()