import pygame
from pygame.sprite import Sprite
import random



class PowerUp(Sprite):
    """A class that manages the power ups for the game"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/power_up.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0
        
        self.y = float(self.rect.y)
        self.speed = self.settings.powerup_speed

    def update(self):
        self.y += self.speed
        self.rect.y = self.y


    def draw_powerup(self):
        self.screen.blit(self.image, self.rect)




class HealthPowerUp(Sprite):
    """A class that manages the health power-ups for the game"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/health.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = 0

        self.y = float(self.rect.y)
        self.speed = self.settings.powerup_speed

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_powerup(self):
        self.screen.blit(self.image, self.rect)