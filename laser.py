import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, group, position) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (position))