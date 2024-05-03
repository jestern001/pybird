from tkinter import Canvas

from gamesettings import GameObjectFactory, RoomConfig
from gameobjects.gameobject import GameObject
from inputlistener import InputListener


class Room:
    def __init__(
        self,
        canvas: Canvas,
        input_listener: InputListener,
        room_settings: RoomConfig
    ) -> None:
        self.canvas = canvas
        self.input_listener = input_listener

        # set window title
        self.canvas.winfo_toplevel().title()

        # build game objects form config
        self.game_objects: dict[int, GameObject] = {}
        for game_object_data in room_settings.game_objects:
            game_object = GameObjectFactory.get(game_object_data)

            # if there's an image, draw it
            if game_object.image_path is not None:
                room_id = self.canvas.create_image(
                    game_object.x,
                    game_object.y,
                    image=game_object.sprite
                )

            # if there's no image, draw a rectangle
            else:
                room_id = self.canvas.create_rectangle(
                    game_object.x,
                    game_object.y,
                    game_object.x+game_object.w,
                    game_object.y+game_object.h,
                    fill=game_object.fill
                )

            self.game_objects[room_id] = game_object

        # self.photo_image = PhotoImage(file="Sprites/CharacterPlaceholder.gif")
        # self.canvas.create_image(100, 100, image=self.photo_image)

    def update(self):

        # update all room objects
        for room_id, obj in self.game_objects.items():

            # move player
            inputs = self.input_listener.key_pressed
            obj.update(inputs=inputs, game_objects=self.game_objects.values())

            # move
            self.canvas.move(room_id, obj.x - obj.x_previous, obj.y - obj.y_previous)
