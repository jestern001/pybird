from colors import Colors
from inputlistener import InputListener
from room import Room


from tkinter import Canvas, Tk


class App:
    def __init__(self, update_rate = 1000//30) -> None:
        # set tk
        self.tk = Tk()
        self.canvas = Canvas(self.tk, bg=Colors.GREEN)
        self.canvas.pack()

        # set up game
        self.input_listener = InputListener(self.tk)
        self.room = Room(self.canvas, self.input_listener)
        self.update_rate = update_rate

        # set up game loop
        self.game_loop()

    def game_loop(self):
        self.room.update()
        self.tk.after(self.update_rate, self.game_loop)

    def run(self):
        self.tk.mainloop()