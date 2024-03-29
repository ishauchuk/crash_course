
class Settings:
	"""Класс для хранения настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует настройки игры"""

		# Параметры экрана
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Параметры снаряда
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Настройка корабля
		self.ship_speed = 1.5

		# Насройка пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 1
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1
