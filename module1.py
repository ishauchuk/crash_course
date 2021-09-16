
class User():
	"""Make some users base"""

	def __init__(self, first_name, last_name, age, nickname):
		"""Инициализируем атрибуты"""
		self.first_name = first_name
		self.last_name = last_name
		self. age = age
		self.nickname = nickname

	def describe_user(self):
		print(f"\
\n{self.first_name} {self.last_name} with nickname '{self.nickname}' \
is {self.age} years old.")

	def greet_user(self):
		print(f"Hello {self.nickname}. How do you do?")