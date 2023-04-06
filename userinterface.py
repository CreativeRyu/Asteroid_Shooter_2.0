import pygame
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Score:
    def __init__(self):
        self.font = pygame.font.Font("ressources/graphics/subatomic.ttf", 30)
    
    def show_score(self, display):
        score_text = f"Score: {pygame.time.get_ticks() // 1000}"
        text_surf = self.font.render(score_text, True,(255,255,255))
        text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 7, WINDOW_HEIGHT - 40))
        display.blit(text_surf, text_rect)
        pygame.draw.rect(display, (255,255,255), text_rect.inflate(30, 30), width = 5, border_radius= 5)