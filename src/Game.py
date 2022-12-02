import pygame
from pygame.rect import Rect

from Food import Food
from Point import Point
from Cobra import Cobra


class Game:
    block_size = 20

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Golden Cobra")
        self.cobra = Cobra(Point(width // 2, height // 2), self.block_size)
        self.food = Food(width, height, self.block_size)

    def get_correct_point(self, point: Point):
        if point.x < 0:
            point.x = self.width
        elif point.x >= self.width:
            point.x = 0
        if point.y < 0:
            point.y = self.height
        elif point.y >= self.height:
            point.y = 0
        return point

    def listen(self, event: pygame.event):
        match event.key:
            case pygame.K_LEFT:
                self.cobra.set_direction("left")
            case pygame.K_RIGHT:
                self.cobra.set_direction("right")
            case pygame.K_UP:
                self.cobra.set_direction("up")
            case pygame.K_DOWN:
                self.cobra.set_direction("down")
            case pygame.K_a:
                self.move(True)
            case pygame.K_ESCAPE:
                self.cobra.direction = Point(0, 0)
            case pygame.QUIT:
                pygame.quit()

    def draw(self):
        food_point = self.food.point
        pygame.draw.rect(self.window, (255, 0, 0), Rect(food_point.x, food_point.y, self.block_size, self.block_size))
        for point in self.cobra.snake_blocks_coord:
            pygame.draw.rect(self.window, (225, 210, 0), Rect(point.x, point.y, self.block_size, self.block_size))

    def move(self, add_size=False):
        position = self.get_correct_point(self.cobra.position.addition(self.cobra.direction))
        self.cobra.position = position
        is_collision = self.is_food_eating(position)
        self.cobra.move(position, is_collision)
        if is_collision:
            self.food.refresh()

    def is_self_eating(self):
        cobra_coords = self.cobra.snake_blocks_coord
        cobra_head = cobra_coords[-1]
        for cord in cobra_coords[:len(cobra_coords) - 2]:
            if cobra_head == cord:
                return True
        return False

    def is_food_eating(self, position):
        return position == self.food.point
