from module1 import *


class Admin(User):
	"""Представляет собой вид пользователя с особыми правами"""

	def __init__(self, first_name, last_name, age, nickname):
		"""Инициализирует атрибуты класса-родителя."""

		super().__init__(first_name, last_name, age, nickname)
		self.privileges = Privileges(self.first_name, self.nickname)


class Privileges():

	def __init__(self, first_name, nickname):
		"""Расширенные права для админов"""

		# super().__init__(self)
		self.privileges = [
							'разрешено добавлять пользователя',
							'разрешено удалять пользователя',
							'разрешено банить пользователя',
							'разрешено выполнять модерацию',
						]		
		self.first_name = first_name
		self.nickname = nickname

	def show_privileges(self):
		print(f"\nAdmin {self.first_name} '{self.nickname}' could do:")
		for privilege in self.privileges:
			print("\t - " + privilege)