import pygame
import game_settings as gs

class Score:
    def __init__(self):
        self.font = pygame.font.Font("ressources/graphics/subatomic.ttf", 30)
        self.title_font = pygame.font.Font("ressources/graphics/subatomic.ttf", 50)
        self.start_font = pygame.font.Font("ressources/graphics/subatomic.ttf", 20)
    
    def show_title(self, display):
        title_surf = self.title_font.render("Space Boi", True, "White")
        title_rect = title_surf.get_rect(midtop = (640, 150))
        start_surf = self.start_font.render("Press Mouse Button", True, "White")
        start_rect = start_surf.get_rect(midtop = (640, 230))
        display.blit(title_surf, title_rect)
        display.blit(start_surf, start_rect)
        pygame.draw.rect(display, (255,255,255), title_rect.inflate(30, 30), width = 5, border_radius= 5)
        
    def show_score(self, display):
        score_text = f"Score: {gs.SCORE}"
        text_surf = self.font.render(score_text, True,(255,255,255))
        text_rect = text_surf.get_rect(midbottom = (gs.WINDOW_WIDTH / 7, gs.WINDOW_HEIGHT - 40))
        display.blit(text_surf, text_rect)
        pygame.draw.rect(display, (255,255,255), text_rect.inflate(30, 30), width = 5, border_radius= 5)