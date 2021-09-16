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

user_1 = User("Alex", "Dukhvalov", 29, "Duh")
user_2 = Admin("Serg", "Charnukha", 28, "Cherny")

user_list = [user_1, user_2]

for user in user_list:
	user.describe_user()
	user.greet_user()

user_2.privileges.show_privileges()
