from Point import Point
import random

class Food:
    def __init__(self, x, y, block_size):
        self.x = x // block_size - 1
        self.y = y // block_size - 1
        self.size = block_size
        self.refresh()

    def refresh(self):
        self.point = Point(random.randint(0, self.x) * self.size, random.randint(0, self.y) * self.size)