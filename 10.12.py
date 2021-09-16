import json

def get_number():
	"""Получает число, если оно сохранено"""

	filename = 'number.json'
	try:
		with open(filename) as f:
			number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return number

def get_new_number():
	"""Запрашивает новое число"""

	number = int(input('What is your favorite number? '))
	filename = 'number.json'
	with open(filename, 'w') as f:
		json.dump(filename, f)
	return number

def output_message():
	"""Выводит загаданное число"""

	number = get_number()
	if number:
		print(f"I know your favorite number! It is '{number}'.")
	else:
		number = get_new_number()
		print(f"I know your favorite number! It is '{number}'.")

output_message()