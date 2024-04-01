import json
from pathlib import Path
from tkinter import Canvas, Widget
from typing import Callable

from colors import Colors
from inputlistener import InputListener, Keys
from point import Point
from tags import Tags


class Room:
    def __init__(self, app: Widget, file_path: Path, grid_size: int, inputs: InputListener, move_speed: float) -> None:
        room_data = json.loads(file_path.read_text())

        # build the canvas
        height = room_data['height']
        width = room_data['width']
        fill = room_data['fill']
        self.canvas = Canvas(
            master=app,
            width=width,
            height=height,
            background=fill
        )
        self.canvas.pack()

        # settings
        self.grid_size = grid_size
        self.inputs = inputs
        self.move_speed = move_speed

        # add objects
        for obj in room_data['objs']:
            x, y = obj.get('location', (0, 0))
            h, w = obj.get('size', (grid_size, self.grid_size))
            fill = obj.get('fill', Colors.GREEN)
            tags = obj.get('tags', [])
            self.canvas.create_rectangle(
                x, y, x+w, y+h,
                fill=fill,
                tags=tags
            )

    def update(self):
        # move player
        player = self.get_from_tag(Tags.PLAYER)
        if player:
            if self.inputs.key_pressed(Keys.LEFT):
                self.move_obj(player, Point(-1*self.move_speed, 0))
            if self.inputs.key_pressed(Keys.RIGHT):
                self.move_obj(player, Point(self.move_speed, 0))
            if self.inputs.key_pressed(Keys.UP):
                self.move_obj(player, Point(0, -1*self.move_speed))
            if self.inputs.key_pressed(Keys.DOWN):
                self.move_obj(player, Point(0, self.move_speed))
        self.canvas.update()
    
    def move_obj(self, obj: int, offset: Point):
        self.canvas.move(obj, offset.x, offset.y)

    def get_from_tag(self, tag: str) -> list[int]:
        return list(self.canvas.find_withtag(tag))

    def after(self, speed: float, method: Callable):
        self.canvas.after(speed, method)
