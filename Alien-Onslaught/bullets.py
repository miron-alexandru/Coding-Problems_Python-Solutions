import pygame
import random
from pygame.sprite import Sprite



class Thunderbolt(Sprite):
    """A class to manage bullets for the Player 1 ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/blue.png')
        self.image = pygame.transform.scale(self.image, (35, 30))
        self.rect = self.image.get_rect()
        self.rect.midtop = (ai_game.first_player_ship.rect.centerx, ai_game.first_player_ship.rect.top)


        self.y = float(self.rect.y)   # Store the bullet's position as a decimal value.

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.first_player_bullet_speed   # Update bullet decimal position
        self.rect.y = self.y   # Update bullet rect position.

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)


class Firebird(Thunderbolt):
    """A class to manage bullets for the Player 2 ship."""
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/red.png')
        self.image = pygame.transform.scale(self.image, (35, 30))
        self.rect = self.image.get_rect()
        self.rect.midtop = (ai_game.second_player_ship.rect.centerx, ai_game.second_player_ship.rect.top)

        self.y = float(self.rect.y)
        
        
    def update(self):
        self.y -= self.settings.second_player_bullet_speed
        self.rect.y = self.y



class AlienBullet(Sprite):
    """A class to manage bullets for the aliens."""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien_bullet.png')
        self.image = pygame.transform.scale(self.image, (35, 40))
        self.rect = self.image.get_rect()


        random_alien = random.choice(ai_game.aliens.sprites())
        self.rect.centerx = random_alien.rect.centerx
        self.rect.bottom = random_alien.rect.bottom

        self.y = float(self.rect.y)


    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y


    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)



