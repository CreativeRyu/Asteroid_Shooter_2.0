import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, group, position) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (position))
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 400
        
    def update(self, delta_time):
        self.position += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.position.x), round(self.position.y))