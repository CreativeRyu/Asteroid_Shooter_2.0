import pygame
from random import randint, uniform
import game_settings as gs

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/meteor.png").convert_alpha()
        scale_multiplier = uniform(0.5, 1.5)
        asteroid_size = pygame.math.Vector2(self.image.get_size()) * scale_multiplier
        self.scaled_surface = pygame.transform.scale(self.image, (asteroid_size))
        self.image = self.scaled_surface
        self.x_cor = randint(-100, gs.WINDOW_WIDTH + 100)
        self.y_cor = randint(-100, -50)
        self.position = self.x_cor, self.y_cor
        self.rect = self.image.get_rect(center = (self.position))
        self.mask = pygame.mask.from_surface(self.image)
        
        # Float Based Position
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(200, 400)
        
        # Rotation Logic
        self.rotation = 0
        self.rotation_speed = randint(10, 30)
        
    def rotate(self, delta_time):
        self.rotation += self.rotation_speed * delta_time
        rotated_image = pygame.transform.rotozoom(self.scaled_surface, self.rotation, 1)
        self.image = rotated_image
        self.rect = self.image.get_rect(center = self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, delta_time):
        self.position += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.position.x), round(self.position.y))
        if self.rect.top > gs.WINDOW_HEIGHT:
            self.kill()
        self.rotate(delta_time)