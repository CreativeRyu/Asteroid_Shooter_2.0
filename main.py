import sys
import pygame
from spaceship import SpaceShip
from laser import Laser

pygame.init()
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter 2.0 OOP")
game_clock = pygame.time.Clock()
background = pygame.image.load("ressources/graphics/background.png").convert()

# Sprite Groups
ship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()

# Ship Creation
ship = SpaceShip(ship_group)
laser = Laser(laser_group,(0,300))

# Game Loop
while True:
    
    # Event Loop
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Delta Time
    delta_time = game_clock.tick(FPS) / 1000
    
    # update
    ship_group.update()
    
    # Update graphics
    display.blit(background, (0,0))
    ship_group.draw(display)
    laser_group.draw(display)

    # show current Frame
    pygame.display.update()