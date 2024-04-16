from dataclasses import dataclass
from typing import Union


@dataclass
class Point:
    x: float
    y: float

    def __add__(self, offset: 'Point'):
        return Point(self.x+offset.x, self.y+offset.y)
    
    def __mul__(self, scale: float):
        return Point(self.x*scale, self.y*scale)


@dataclass
class Location:
    x1: float
    y1: float
    x2: float
    y2: float

    @property
    def x(self) -> float:
        return self.x1
    
    @property
    def y(self) -> float:
        return self.x2
    
    @property
    def point(self) -> Point:
        return Point(self.x, self.y)
    
    @property
    def width(self) -> float:
        return abs(self.x2 - self.x1)
    
    @property
    def height(self) -> float:
        return abs(self.y2 - self.y1)
    
    @property
    def size(self) -> Point:
        return Point(self.width, self.height)

    def from_coords(coords: tuple[float, float, float, float]) -> 'Location':
        return Location(*coords)
    
    def as_coords(self) -> tuple[float, float, float, float]:
        return (
            self.x1,
            self.y1,
            self.x2,
            self.y2
        )
    
    def __add__(self, offset: Union[int, Point, 'Location']) -> 'Location':
        if isinstance(offset, int):
            return Location(
                self.x1 + offset,
                self.y1 + offset,
                self.x2 + offset,
                self.y2 + offset
            )

        if isinstance(offset, Point):
            return Location(
                self.x1 + offset.x,
                self.y1 + offset.y,
                self.x2 + offset.x,
                self.y2 + offset.y
            )

        if isinstance(offset, Location):
            return Location(
                self.x1 + offset.x1,
                self.y1 + offset.y1,
                self.x2 + offset.x2,
                self.y2 + offset.y2
            )
        