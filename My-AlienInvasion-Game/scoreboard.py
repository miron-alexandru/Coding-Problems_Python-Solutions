import pygame.font
from pygame.sprite import Group
from ships import Ship, SecondShip
from heart import Heart



class ScoreBoard:
	"""A class to report scoring information."""
	def __init__(self, ai_game):
		"""Initialize scorekeeping attributes."""
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		self.second_stats = ai_game.second_stats

		#Font settings for scoring information.
		self.text_color = (255, 0, 0)
		self.font = pygame.font.SysFont(None, 48)

		#Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score)
		rounded_second_score = round(self.second_stats.second_score)
		score_str = "{:,}".format(rounded_score)
		second_score_str = "{:,}".format(rounded_second_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.settings.bg_color)
		self.second_score_image = self.font.render(second_score_str, True,
			self.text_color, self.settings.bg_color)

		#Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -20
		self.score_rect.top = 20

		self.second_score_rect = self.second_score_image.get_rect()
		self.second_score_rect.right = self.screen_rect.right - 120
		self.second_score_rect.top = 20
		

	def prep_high_score(self):
		"""Turn the high score intro a rendered image."""
		high_score = round(self.stats.high_score)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.settings.bg_color)

		#Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score + self.second_stats.second_score > self.stats.high_score:
			self.stats.high_score = self.stats.score + self.second_stats.second_score
			self.prep_high_score()

	def prep_level(self):
		"""Turn the level into a rendered image."""
		level_str = str(self.stats.level)
		self.level_image = self.font.render(level_str,True,
			self.text_color,self.settings.bg_color)

		#Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Show how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Heart(self.ai_game, 0, 0)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


	def show_score(self):
		"""Draw scores, level and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.second_score_image, self.second_score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
