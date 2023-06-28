import sys
import pygame
from spaceship import SpaceShip
from asteroid import Asteroid
from userinterface import Score
from upgrade import Upgrade
import game_settings as gs

pygame.init()

display = pygame.display.set_mode((gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter 2.0 OOP")
game_clock = pygame.time.Clock()
background = pygame.image.load("ressources/graphics/background.png").convert()
game_music = pygame.mixer.Sound("ressources/sounds/music.wav")
is_game_on = False

# Asteroid Timer
asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 1400)

# Sprite Groups
ship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
upgrade_group = pygame.sprite.Group()

# Object Declaration
ship = SpaceShip(ship_group)
score = Score()
upgrade = Upgrade(upgrade_group)

game_music.play(loops = -1)

# Game Loop
while True:
    
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not is_game_on:
            is_game_on = True
        
        if event.type == asteroid_timer:
            asteroid = Asteroid(asteroid_group)

    # Delta Time
    delta_time = game_clock.tick(gs.FPS) / 1000
    
    # update
    ship_group.update(laser_group, upgrade_group)
    laser_group.update(delta_time, asteroid_group)
    asteroid_group.update(delta_time)
    upgrade_group.update(delta_time)
    
    # Update graphics
    if not is_game_on:
        display.blit(background, (0,0))
        ship_group.draw(display)
        score.show_title(display)
        score.show_score(display)
    else:
        display.blit(background, (0,0))
        upgrade_group.draw(display)
        ship_group.draw(display)
        laser_group.draw(display)
        asteroid_group.draw(display)
        score.show_score(display)
        
    # show current Frame
    pygame.display.update()