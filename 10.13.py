import json


def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует."""

	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Запрашивает новое имя пользователя."""

	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username


def greet_user():
	"""Приветствует пользователя по имени."""

	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

def name_checking():
	"""Проверка последнего пользователя"""

	filename = 'username.json'
	with open(filename) as f:
		last_user = json.load(f)
	choice = input(f"Last user is {last_user}. Is it you?(Enter 'yes' for yourself)\n")
	if choice == 'yes':
		greet_user()
	else:
		get_new_username()
		greet_user()


name_checking()