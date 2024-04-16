from gameobject import GameObject
from old.inputlistener import Keys


class Player(GameObject):
    def update(self, inputs: dict[str, bool]):
        left = inputs.get(Keys.LEFT)
        right = inputs.get(Keys.RIGHT)
        up = inputs.get(Keys.UP)
        down = inputs.get(Keys.DOWN)

        # get new direction
        dir_x = 0
        dir_y = 0
        if left: dir_x -= 1
        if right: dir_x += 1
        if up: dir_y -= 1
        if down: dir_y += 1

        # scale new direction
        move_speed = self.move_speed
        x_offset = dir_x * move_speed
        y_offset = dir_y * move_speed

        # apply offsets
        self.x_previous = self.x
        self.y_previous = self.y
        self.x += x_offset
        self.y += y_offset

        super().update()