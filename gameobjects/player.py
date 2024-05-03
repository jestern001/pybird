import logging
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

        # handle x collisions
        collisions = self.get_collisions(x_new, self.y, x_new + self.w, self.y + self.h, game_objects)
        if collisions:
            sorted_collisions = sorted(collisions, key = lambda c: abs(c.x - self.x))
            closest_collision = sorted_collisions[0]
            if closest_collision.x < self.x:
                x_new = closest_collision.x + closest_collision.w + 1
            elif self.x < closest_collision.x:
                x_new = closest_collision.x - self.w -1
            else:
                x_new += 1

        # handle y collisions
        collisions = self.get_collisions(self.x, y_new, self.x + self.w, y_new + self.h, game_objects)
        if collisions:
            sorted_collisions = sorted(collisions, key = lambda c: abs(c.y - self.y))
            closest_collision = sorted_collisions[0]
            if closest_collision.y < self.y:
                y_new = closest_collision.y + closest_collision.w + 1
            elif self.y < closest_collision.y:
                y_new = closest_collision.y - self.w - 1
            else:
                y_new += 1

        # apply offsets
        self.x = x_new
        self.y = y_new
