import pygame
from pygame.sprite import Sprite
import random



class PowerUp(Sprite):
    """A class that manages the power ups for the game"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.powerup_color

        self.rect = pygame.Rect(0, 0, self.settings.powerup_width, self.settings.powerup_height)
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0
        
        self.y = float(self.rect.y)
        self.speed = self.settings.powerup_speed

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_powerup(self):
        pygame.draw.rect(self.screen, self.color, self.rect)