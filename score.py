import pygame.font
from pygame import Surface


class Score:
    def __init__(self, font_size=36, color=(255, 255, 0)):
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color

    def increase(self, points=1) -> None:
        self.score += points

    def reset(self):
        self.score = 0
    
    def draw(self, screen: Surface, x: int, y: int):
        score_text = self.font.render(f"SCORE: {self.score}", False, self.color)
        screen.blit(score_text, (x, y))