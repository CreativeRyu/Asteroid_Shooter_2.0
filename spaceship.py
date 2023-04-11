import pygame
from laser import Laser
import game_settings as gs

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.can_fire = True
        self.time_of_fire = None
        self.image = pygame.image.load("ressources/graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center = (gs.WINDOW_WIDTH / 2, gs.WINDOW_HEIGHT / 2))
        self.mask = pygame.mask.from_surface(self.image)
        self.laser_sound = pygame.mixer.Sound("ressources/sounds/laser.ogg")
    
    # Timer zur limitierung des Lasers
    def fire_timer(self):
        if not self.can_fire:
            current_time = pygame.time.get_ticks()
            if current_time - self.time_of_fire > 500:
                self.can_fire = True
    
    def move(self):
        self.rect.center = pygame.mouse.get_pos()
    
    def fire_laser(self, laser_group):
        if pygame.mouse.get_pressed()[0] and self.can_fire:
            self.can_fire = False
            self.time_of_fire = pygame.time.get_ticks()
            Laser(laser_group, self.rect.midtop)
            self.laser_sound.play()
    
    # def asteroid_collision(self, asteroid_group):
    #     if pygame.sprite.spritecollide(self, asteroid_group, True):
    #         pygame.quit()
    #         sys.exit()
    
    def update(self, laser_group):
        self.move()
        self.fire_timer()
        self.fire_laser(laser_group)