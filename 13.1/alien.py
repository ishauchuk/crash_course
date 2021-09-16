import pygame 
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
	"""Класс, представляющий одного пришельца."""

	def __init__(self, ai_game):
		"""Инициализирует одного пришельца и задает начальную позицию."""
		super().__init__()
		self.screen = ai_game.screen
		self.random_number = randint(-50, 50)

		# Загрузка изображения пришельца и назначение атрибута rect.
		self.image = pygame.image.load('images/alien.png')
		self.image = pygame.transform.scale(self.image, (75, 75))
		self.rect = self.image.get_rect()

		# Каждый новый пришелец появляется в левом верхнем углу экрана.
		self.rect.x = self.rect.width + self.random_number
		self.rect.y = self.rect.height + self.random_number

		# Сохранение точной горизонтальной позиции пришельца.
		self.x = float(self.rect.x)