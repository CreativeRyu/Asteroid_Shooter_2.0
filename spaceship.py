import pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("ressources/graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))