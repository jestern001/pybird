from gameobject import GameObject
from player import Player
from colors import Colors


from tkinter import Canvas, Tk

from inputlistener import InputListener


class Room:
    def __init__(self, canvas: Canvas, input_listener: InputListener) -> None:
        self.canvas = canvas
        self.input_listener = input_listener

        # create game objects
        game_objects = [
            Player(
                x=50,
                y=50,
                h=15,
                w=15,
                fill=Colors.ORANGE,
                tags=["player"],
                move_speed=3
            )
        ]

        # draw game objects
        self.game_objects: dict[int, GameObject] = {}
        for game_object in game_objects:
            room_id = self.canvas.create_rectangle(
                game_object.x,
                game_object.y,
                game_object.x+game_object.w,
                game_object.y+game_object.h,
                fill=game_object.fill,
                tags=game_object.tags
            )
            self.game_objects[room_id] = game_object

    def update(self):
        # update all room objects
        for room_id, game_object in self.game_objects.items():

            # update location
            coords = self.canvas.coords(room_id)
            game_object.x = coords[0]
            game_object.y = coords[1]
            game_object.w = coords[2]-coords[0]
            game_object.h = coords[3]-coords[1]

            # handle player movement
            if isinstance(game_object, Player):
                # move player
                inputs = self.input_listener.key_pressed
                game_object.update(inputs)

                # move
                self.canvas.move(
                    room_id,
                    game_object.x - game_object.x_previous,
                    game_object.y - game_object.y_previous
                )