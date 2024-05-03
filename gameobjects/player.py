from math import copysign
from pathlib import Path
from gameobjects.gameobject import GameObject
from old.inputlistener import Keys


class Player(GameObject):
    def update(
        self,
        inputs: dict[str, bool],
        game_objects: list['GameObject'] = []
    ):
        # call generic object logic
        super().update()

        # get input values
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

        # set new position
        x_new = self.x + x_offset
        y_new = self.y + y_offset

        # handle collisions
        collisions = self.get_collisions(x_new, y_new, x_new + self.w, y_new + self.h, game_objects)
        for collision in collisions:

            # move close to and around collision
            if self.x < collision.x:
                self.x = collision.x-self.w
                x_offset = 0
            elif collision.x < self.x:
                self.x = collision.x + collision.w
                x_offset = 0
            elif self.y < collision.y:
                self.y = collision.y-self.h
                y_offset = 0
            elif collision.y < self.y:
                self.y = collision.y + collision.h
                y_offset = 0

        # apply offsets
        self.x += x_offset
        self.y += y_offset
