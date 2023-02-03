import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""A class to manage the ship."""

	def __init__(self,ai_game,x, y):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect(topleft = (227, 592))


		#Start each new ship at the bottom center of the screen.
		#self.rect.midbottom = self.screen_rect.midbottom

		#Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		#Update the ship's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.ship_speed


		#Update rect object from self.x.
		self.rect.x = self.x - 250
		self.rect.y = self.y
			

	def blitme(self):
			"""Draw the ship at its current location."""
			self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)	




class SecondShip(Ship):
	def __init__(self, ai_game,x, y):
		super().__init__(ai_game, x, y)
		self.moving_right = False
		self.moving_left = False
		self.moving_upp = False
		self.moving_downn = False
		self.image = pygame.image.load('images/ship4.png')
		self.rect = self.image.get_rect(topleft = (727, 592))

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		if self.moving_upp and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_downn and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		#Update rect object from self.x.
		self.rect.x = self.x + 250
		self.rect.y = self.y