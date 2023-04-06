import sys
import pygame
from spaceship import SpaceShip
from asteroid import Asteroid
from userinterface import Score

pygame.init()
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter 2.0 OOP")
game_clock = pygame.time.Clock()
background = pygame.image.load("ressources/graphics/background.png").convert()

# asteroid timer
asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 1400)

# Sprite Groups
ship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()

# Ship Creation
ship = SpaceShip(ship_group)
score = Score()

# Game Loop
while True:
    
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == asteroid_timer:
            asteroid = Asteroid(asteroid_group)
    
    # Delta Time
    delta_time = game_clock.tick(FPS) / 1000
    
    # update
    ship_group.update(laser_group)
    laser_group.update(delta_time, asteroid_group)
    asteroid_group.update(delta_time)
    
    # Update graphics
    display.blit(background, (0,0))
    ship_group.draw(display)
    laser_group.draw(display)
    asteroid_group.draw(display)
    score.show_score(display)
    
    # show current Frame
    pygame.display.update()