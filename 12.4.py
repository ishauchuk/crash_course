import sys
import pygame 
import json

class EmptyDisplay:

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Empty Display")
		self.bg_color = (0, 0, 0)

	def run_app(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self._check_events()
			self.screen.fill(self.bg_color)
			pygame.display.flip()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.key == pygame.K_RIGHT:
				# if event.key == pygame.K_RIGHT:
					# print(event.key)
				filename = 'key.json'
				with open(filename, 'w') as f:
					json.dump(int(event.key), f)



if __name__ == '__main__':
	EmptyDisplay().run_app()