import pygame



class Settings:
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's static settings."""
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		self.bg_img = pygame.image.load('images/space.jpg')


		#Ships settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		#First bullet settings
		self.bullet_speed = 3.0
		self.bullet_width = 300
		self.bullet_height = 10
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 3
		
		#Second bullet settings
		self.second_bullet_width = 300
		self.second_bullet_height = 10


		#Alien settings
		self.alien_speed = 0.5
		self.fleet_drop_speed = 1

		#How quickly the game speeds up
		self.speedup_scale = 1.1

		#How quickly the alien point values increase
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		#fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 15	

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed += self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)