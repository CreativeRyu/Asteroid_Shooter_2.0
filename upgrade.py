import pygame
import game_settings as gs

class Upgrade(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/Bullet.png").convert_alpha()
        image_size = pygame.math.Vector2(self.image.get_size()) * 3
        self.scaled_image = pygame.transform.scale(self.image, (image_size))
        self.image = self.scaled_image
        self.rect = self.image.get_rect(midbottom = (gs.WINDOW_WIDTH//2, - 20))
        self.mask = pygame.mask.from_surface(self.image)
    
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, 1)
        self.speed = 200

    def update(self, delta_time):
        if gs.SCORE >= 10:
            self.position += self.direction * self.speed * delta_time
            self.rect.topleft = (round(self.position.x), round(self.position.y))
            
            # Removes Lasers on top of the screen
            if self.rect.top > gs.WINDOW_HEIGHT:
                self.kill()