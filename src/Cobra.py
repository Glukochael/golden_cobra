from pygame.rect import Rect
from Point import Point


class Cobra:
    direction: Point
    snake_blocks_coord = []
    snake_size = 3
    speed: int

    def __init__(self, point: Point, speed: int):
        for _ in range(self.snake_size - 1, -1, -1):
            self.snake_blocks_coord.append(Point(point.x, point.y + speed * _))
        self.position = point
        self.__directions = {"up": Point(0, -speed), "down": Point(0, speed),
                             "left": Point(-speed, 0), "right": Point(speed, 0)}
        self.speed = speed
        self.direction = self.__directions["up"]

    def set_direction(self, direction: str):
        if self.direction == self.__directions[direction].multiplication(-1):
            return
        self.direction = self.__directions[direction]

    def move(self, point: Point, add_size: bool = False):
        if self.direction == Point(0, 0):
            return
        self.snake_blocks_coord.append(point)
        if add_size:
            self.snake_size += 1
            return
        del self.snake_blocks_coord[0]
