import pygame.font
from pygame.sprite import Group
from ships import Thunderbird, Phoenix
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
		self.font = pygame.font.SysFont(None, 30)

		#Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_hp()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score)
		rounded_second_score = round(self.second_stats.second_score)
		score_str = "{:,}".format(rounded_score)
		second_score_str = "{:,}".format(rounded_second_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, None)
		self.second_score_image = self.font.render(second_score_str, True,
			self.text_color, None)

		# Display the scores at the stop right of the screen.
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
			self.text_color, None)

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
			self.text_color,None)

		#Position the level below the score.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_hp(self):
		self.hearts = Group()
		for heart_number in range(self.stats.ships_left):
			heart = Heart(self.ai_game, 0, 0)
			heart.rect.x = 10 + heart_number * heart.rect.width
			heart.rect.y = 10
			self.hearts.add(heart)


	def show_score(self):
		"""Draw scores, level and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.second_score_image, self.second_score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.hearts.draw(self.screen)


class SecondScoreBoard(ScoreBoard):
	"""A class to report scoring information for the single player mode."""
	def __init__(self, ai_game):
		super().__init__(ai_game)

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, None)

		# Display the score at the stop right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -20
		self.score_rect.top = 20
		
	def prep_high_score(self):
		"""Turn the high score intro a rendered image."""
		high_score = round(self.stats.high_score)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, None)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score  > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def show_score(self):
		"""Draw scores, level and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.hearts.draw(self.screen)

