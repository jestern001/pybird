from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def __add__(self, offset: 'Point'):
        return Point(self.x+offset.x, self.y+offset.y)
    
    def __mul__(self, scale: float):
        return Point(self.x*scale, self.y*scale)