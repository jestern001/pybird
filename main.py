from app import App


GRID_SIZE = 32
ROOM_SPEED = 1000 // 30 # set to 30 frames per second
MOVE_SPEED = 5


if __name__ == "__main__":
    # start the game
    app = App(grid_size = GRID_SIZE, room_speed = ROOM_SPEED, move_speed = MOVE_SPEED)
    app.start()