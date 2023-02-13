import pygame
from pygame.sprite import Sprite



class Thunderbolt(Sprite):
	"""A class to manage bullets for the Player 1 ship"""
	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.first_player_bullet_color

		self.rect = pygame.Rect(0,0, self.settings.first_player_bullet_width,   # Create a bullet rect at (0,0) and then set correct position.
			self.settings.first_player_bullet_height)
		self.rect.midtop = ai_game.first_player_ship.rect.midtop 

		self.y = float(self.rect.y)   # Store the bullet's position as a decimal value.

	def update(self):
		"""Move the bullet up the screen."""
		self.y -= self.settings.first_player_bullet_speed   # Update bullet decimal position
		self.rect.y = self.y   # Update bullet rect position.

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen,self.color,self.rect)


class Firebird(Thunderbolt):
	"""A class to manage bullets for the Player 2 ship."""
	def __init__(self, ai_game):
		super().__init__(ai_game)
		self.rect = pygame.Rect(0,0, self.settings.second_player_bullet_width,
			self.settings.second_player_bullet_height)
		self.rect.midtop = ai_game.second_player_ship.rect.midtop
		self.color = self.settings.second_player_bullet_color
		
		
	def update(self):
		self.y -= self.settings.second_player_bullet_speed
		self.rect.y = self.y
