import sys
import pygame
from spaceship import SpaceShip

pygame.init()
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter 2.0 OOP")
game_clock = pygame.time.Clock()

# Sprite Groups
ship_group = pygame.sprite.Group()

# Ship Creation
ship = SpaceShip()
ship_group.add(ship)

# Game Loop
while True:
    
    # Event Loop
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Delta Time
    delta_time = game_clock.tick(FPS) / 1000
    
    # Update graphics
    ship_group.draw(display)

    # show current Frame
    pygame.display.update()