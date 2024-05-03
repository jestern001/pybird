from dataclasses import dataclass
from pathlib import Path
from tkinter import PhotoImage

from resources.colors import Colors


@dataclass
class GameObject:
    # arguments set from settings file
    x: float=0
    y: float=0
    w: float=10
    h: float=10
    x_previous: float=x
    y_previous: float=y
    fill: str = Colors.WHITE
    move_speed: float = 0
    solid: bool = False
    image_location: str | None = None

    # initialized but not set form settings file
    sprite: PhotoImage | None = None
    image_path: Path | None = None

    def __post_init__(self) -> None:
        # convert image path string into a path object
        if self.image_location:
            self.image_path = Path(self.image_location)

    def overlap(self, a0, a1, b0, b1):
        if a0 == a1 or b0 == b1:
            return False
        return a0 <= b1 and b0 <= a1

    def get_collisions(self, x0: float, y0: float, x1: float, y1: float, game_objects: list['GameObject']) -> 'list[GameObject]':
        collisions: list['GameObject'] = []
        for obj in game_objects:
            if obj is self:
                continue
            if (self.overlap(x0, x1, obj.x, obj.x+obj.w)) and (self.overlap(y0, y1, obj.y, obj.y+obj.h)):
                collisions.append(obj)
        return collisions

    def get_collision(self, x0: float, y0: float, x1: float, y1: float, game_objects: list['GameObject']) -> 'GameObject':
        for obj in game_objects:
            if obj is self:
                continue
            if (self.overlap(x0, x1, obj.x, obj.x+obj.w)) and (self.overlap(y0, y1, obj.y, obj.y+obj.h)):
                return obj

    def update(self, **kwargs):
        """Sets x_previous and y_previous to the current x and y, respectivly
        """
        self.x_previous = self.x
        self.y_previous = self.y
