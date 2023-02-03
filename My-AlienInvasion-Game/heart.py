import pygame

from ships import Ship

class Heart(Ship):
	def __init__(self, ai_game, x, y):
		Ship.__init__(self, ai_game, x, y)
		self.image = pygame.image.load('images/heart.png')
		self.rect = self.image.get_rect(topleft = (0, 0))