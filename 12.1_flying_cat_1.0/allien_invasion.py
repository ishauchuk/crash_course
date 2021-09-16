import sys
import pygame
from settings import Settings
from ship import Ship

class AllienInvasion:
	"""Класс для управления ресурсами и поведением игры"""

	def __init__(self):
		"""Инициализирует игру и создает игровые ресурсы."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Cat Hot Dog")

		self.ship = Ship(self)

		# Назначение цвета фона.

	def run_game(self):
		"""Запуск основного цикла игры."""
		while True:
			self._check_events()			
			self.ship.update()
			self._update_screen()

	def _check_events(self):
		"""Обрабаотывает нажатия клавиш и события мыши."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self.check_keyup_events(event)

	def check_keydown_events(self, event):
		"""Реагирует на нажатие клавиш."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True


	def check_keyup_events(self, event):
		"""Реагирует на нажатие клавиш."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

	def _update_screen(self):
		"""Обновляет изображения на экране и отображает новый экран."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		# Отображение последнего прорисованного экрана.
		pygame.display.flip()

if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	ai = AllienInvasion()
	ai.run_game()