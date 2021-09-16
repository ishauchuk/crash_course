class User():
	"""Make some users base"""

	def __init__(self, first_name, last_name, age, nickname):
		"""Инициализируем атрибуты"""
		self.first_name = first_name
		self.last_name = last_name
		self. age = age
		self.nickname = nickname
		self.login_attempts = 0

	def describe_user(self):
		print(f"\
\n{self.first_name} {self.last_name} with nickname '{self.nickname}' \
is {self.age} years old.")

	def greet_user(self):
		print(f"Hello {self.nickname}. How do you do?")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print(f"Now number of login attempts is {self.login_attempts}.")

	def reset_login_attempts(self):
		self.login_attempts = 0


user_1 = User("Alex", "Dukhvalov", 29, "Duh")
user_1.describe_user()
user_1.greet_user()
for i in range(3):
	user_1.increment_login_attempts()
print(f"Current number of login attempts {user_1.login_attempts}.")
user_1.reset_login_attempts()
print(f"Current number of login attempts {user_1.login_attempts}.")
