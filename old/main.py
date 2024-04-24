import json
from pathlib import Path
from tkinter import Canvas, Tk, Widget

from inputlistener import InputListener
from tags import Tags
from resources.colors import Colors


GRID_SIZE = 32
ROOM_SPEED = 1000 // 30 # set to 30 frames per second
MOVE_SPEED = 5


def overlaps(x_start: float, x_stop: float, y_start: float, y_stop: float) -> bool:
    if x_start == x_stop or y_start == y_stop:
        return False
    return x_start <= y_stop and y_start <= x_stop


class Room(Canvas):
    def __init__(self, parent: Widget, **kwargs) -> None:
        super().__init__(parent, **kwargs)


class GameObj:
    def __init__(
        self, 
        parent: Canvas, 
        x: float, 
        y: float, 
        w: float = GRID_SIZE, 
        h: float = GRID_SIZE, 
        fill: Colors = Colors.WHITE, 
        tags: list[str] = [],
        layer: int = 0
    ) -> None:
        self.room_id = parent.create_rectangle(
            x,
            y,
            x+w,
            y+h,
            fill=fill,
            tags=tags,
        )
        self.layer = layer


def move_player():
    player = room.find_withtag(Tags.PLAYER)
    if not player:
        return
    x_offset = 0
    y_offset = 0
    if inputs.key_pressed.get("Left"):
        x_offset -= MOVE_SPEED
    if inputs.key_pressed.get("Right"):
        x_offset += MOVE_SPEED
    if inputs.key_pressed.get("Up"):
        y_offset -= MOVE_SPEED
    if inputs.key_pressed.get("Down"):
        y_offset += MOVE_SPEED
    room.move(player, x_offset, y_offset)


# build game
app_data = json.loads(Path("configs/game.json").read_text())
app = Tk()
app.geometry(f"{app_data['height']}x{app_data['width']}")
inputs = InputListener(app)


# populate room
room_data = json.loads(Path("configs/rooms/start.json").read_text())
room = Canvas(width=room_data["width"], height=room_data["height"], bg=Colors.GREEN)
room.pack()
room_objs = room_data["objs"]
room_objs = sorted(room_objs, key=lambda x: x["layer"], reverse=True)
for obj in room_objs:
    GameObj(room, **obj)


# define the game loop
def game_loop():
    move_player()
    room.update()
    room.after(ROOM_SPEED, game_loop)
app.after(ROOM_SPEED, game_loop)

if __name__ == "__main__":
    # start the game
    app.mainloop()