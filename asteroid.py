import pygame
from random import randint, uniform
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/meteor.png").convert_alpha()
        self.x_cor = randint(-100, WINDOW_WIDTH + 100)
        self.y_cor = randint(-100, -50)
        self.position = self.x_cor, self.y_cor
        self.rect = self.image.get_rect(center = (self.position))
        
        # Float Based Position
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
        self.speed = 200
        
    def update(self, delta_time):
        self.position += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.position.x), round(self.position.y))