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
        self.move_player()
        self.canvas.update()
    
    def move_obj(self, obj: int, offset: Point):
        self.canvas.move(obj, offset.x, offset.y)
    
    def get_location(self, obj: int) -> tuple[Point, Point]:
        """Get top corner and size as points

        Args:
            obj (int): The object ID

        Returns:
            tuple[Point, Point]: The top left corner as a point and height and width as a point
        """
        x0, y0, x1, y1 = self.canvas.coords(obj)
        return (Point(x0, y0), Point(x1-x0, y1-y0))

    def get_from_tag(self, tag: str) -> list[int]:
        return list(self.canvas.find_withtag(tag))

    def after(self, speed: float, method: Callable):
        self.canvas.after(speed, method)
    
    def get_room_size(self) -> Point:
        return Point(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqwidth())
    
    def move_player(self):
        # get player
        player = self.get_from_tag(Tags.PLAYER)
        if not player:
            return

        # get move direction
        offset = Point(0, 0)
        if self.inputs.key_pressed(Keys.LEFT):
            offset += Point(-1, 0)
        if self.inputs.key_pressed(Keys.RIGHT):
            offset += Point(1, 0)
        if self.inputs.key_pressed(Keys.UP):
            offset += Point(0, -1)
        if self.inputs.key_pressed(Keys.DOWN):
            offset += Point(0, 1)
        
        # check new location
        room_size = self.get_room_size()
        location, size = self.get_location(player)
        new_location = location + offset

        # stay in room
        if not (0 < new_location.x < room_size.x - size.x):
            offset.x = 0
        if not (0 < new_location.y < room_size.y - size.y):
            offset.y = 0
        
        # move player
        self.move_obj(player, offset * self.move_speed)
