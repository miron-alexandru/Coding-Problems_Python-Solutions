import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width   # Start each new alien near the top left of the screen.
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)   # Store the alien's exact horizontal position.
        self.bullet_chance = 0.01
        self.last_bullet_time = 0

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x



