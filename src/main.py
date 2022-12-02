import pygame
from Game import Game


clock = pygame.time.Clock()
pygame.init()
game = Game(800, 600)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game.listen(event)
    game.window.fill((255, 255, 255))
    game.move()
    game.draw()
    pygame.display.update()
    clock.tick(60)
    pygame.time.wait(60)
    print(game.cobra.direction)
    if game.is_self_eating():
        break
pygame.quit()
