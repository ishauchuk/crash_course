import unittest
from city_functions import country_city

# country_city('belarus', 'minsk')

class CountryCity(unittest.TestCase):
	"""Тесты для 'city_functions.py'."""

	def test_city_country(self):
		"""Страна и город отображаются правильно?"""

		formatted_name = country_city('chile', 'santiago')
		self.assertEqual(formatted_name, '"Santiago, Chile"')


	def test_city_country_population(self):
		"""Страна, город, население отображаются правильно?"""

		formatted_name = country_city('chile', 'santiago', 'population=50000')
		self.assertEqual(formatted_name, '"Santiago, Chile - population population=50000"')

if __name__ == '__main__':
	unittest.main()
