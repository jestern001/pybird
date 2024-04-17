from dataclasses import dataclass, field

from colors import Colors


@dataclass
class GameObject:
    x: float=0
    y: float=0
    w: float=10
    h: float=10
    x_previous: float=x
    y_previous: float=y
    tags: list[str] = field(default_factory=list)
    fill: str = Colors.WHITE
    move_speed: float = 0

    def update(self, **kwargs):
        pass
