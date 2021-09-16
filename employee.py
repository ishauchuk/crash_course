
class Employee():
	"""Сбор данных о соискателе"""

	def __init__(self, name, surname, salary):
		"""Сохраняет имя, фамилию и ежегодный оклад"""
		self.name = name
		self.surname = surname
		self.salary = salary

	def give_raise(self, increase=''):
		if increase:
			int(self.salary)
			self.salary += int(increase)
		else:
			self.salary += 5000
		# print(self.salary)
		return self.salary
