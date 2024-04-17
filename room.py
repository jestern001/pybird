from tkinter import Canvas

from configloader import RoomConfig
from gameobjects.gameobject import GameObject
from colors import Colors
from inputlistener import InputListener
from gameobjects.player import Player


class Room:
    def __init__(self, canvas: Canvas, input_listener: InputListener, room_config: RoomConfig) -> None:
        self.canvas = canvas
        self.input_listener = input_listener

        # set window title
        self.canvas.winfo_toplevel().title()

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
        for room_id, obj in self.game_objects.items():

            # move player
            inputs = self.input_listener.key_pressed
            obj.update(inputs=inputs)

            # move
            self.canvas.move(room_id, obj.x - obj.x_previous, obj.y - obj.y_previous)
