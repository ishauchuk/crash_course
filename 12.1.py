import sys
import pygame


class BlueWindow:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Blue Window")
		self.bw_color = (0, 0, 255)


	def start(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bw_color)

			pygame.display.flip()


class PersPainting():

	def __init__(self, bw_window):
		"""Инициализирует корабль и создает его начальную позицию."""
		self.screen = bw_window.screen
		self.screen_rect = bw_window.screen.get_rect()

if __name__ == '__main__':
	bw = BlueWindow()
	bw.start()