import pygame



class Settings:
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen Settings
		self.screen_size = (1000, 640)
		self.screen_width = 1000
		self.screen_height = 640
		self.bg_color = (0, 0, 0)
		self.bg_img = pygame.image.load('images/space.jpg')
		self.second_bg_img = pygame.image.load('images/space2.png')


		# Ships settings
		self.first_player_ship_speed = 3.0
		self.second_player_ship_speed = 3.0
		self.max_ships = 5
		self.ship_limit = 3

		# First bullet settings
		self.first_player_bullet_speed = 3.0
		self.first_player_bullets_allowed = 3
		
		# Second bullet settings
		self.second_player_bullet_speed = 3.0
		self.second_player_bullets_allowed = 3

		# Alien settings
		self.alien_speed = 0.5
		self.fleet_drop_speed = 1

		# Alien bullet settings
		self.alien_bullet_speed = 0.5

		# PowerUps settings
		self.powerup_speed = 0.5

		# How quickly the game speeds up
		self.speedup_scale = 1.0

		# How quickly the alien point values increase
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

		# 1 represents right, -1 represents left
		self.fleet_direction = 1

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game"""
		self.first_player_ship_speed = 1.5
		self.second_player_ship_speed = 1.5
		self.first_player_bullet_speed = 3
		self.second_player_bullet_speed = 3
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.alien_bullet_speed = 0.5

		# Scoring
		self.alien_points = 15	

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.first_player_ship_speed *= self.speedup_scale
		self.second_player_ship_speed *= self.speedup_scale
		self.first_player_bullet_speed *= self.speedup_scale
		self.second_player_bullet_speed *= self.speedup_scale
		self.alien_speed += self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)
		self.alien_bullet_speed *= self.speedup_scale