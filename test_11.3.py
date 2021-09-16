import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Тесты для класса Employee"""

	def setUp(self):
		self.person_1 = Employee('ihar', 'shauchuk', 300)
		self.person_2 = Employee('ihar', 'shauchuk', 300)
		self.person_final = [5300, 1788]


	def test_give_default_raise(self):
		"""Проверяет, что один ответ сохранен правильно."""
		self.assertEqual(self.person_1.give_raise(), self.person_final[0])

	def test_give_custom_raise(self):
		"""Проверяет, что произвольный оклад сохранен правильно."""
		self.assertEqual(self.person_2.give_raise(1488), self.person_final[1])

if __name__ == '__main__':
	unittest.main()