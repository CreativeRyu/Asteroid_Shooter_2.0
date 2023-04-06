import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, group, position) -> None:
        super().__init__(group)
        self.image = pygame.image.load("ressources/graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (position))
        self.mask = pygame.mask.from_surface(self.image)
        
        # Float Based Position
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 400
    
    def asteroid_collision(self, asteroid_group):
        if pygame.sprite.spritecollide(self, asteroid_group, True, pygame.sprite.collide_mask):
            self.kill()
        
    def update(self, delta_time, asteroid_group):
        self.position += self.direction * self.speed * delta_time
        self.rect.topleft = (round(self.position.x), round(self.position.y))
        
        # Removes Lasers on top of the screen
        if self.rect.bottom < 0:
            self.kill()
        self.asteroid_collision(asteroid_group)