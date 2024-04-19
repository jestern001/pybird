from dataclasses import dataclass

from colors import Colors


@dataclass
class GameObject:
    x: float=0
    y: float=0
    w: float=10
    h: float=10
    x_previous: float=x
    y_previous: float=y
    fill: str = Colors.WHITE
    move_speed: float = 0
    solid: bool = False

    def update(self, **kwargs):
        """Sets x_previous and y_previous to the current x and y, respectivly
        """
        self.x_previous = self.x
        self.y_previous = self.y
