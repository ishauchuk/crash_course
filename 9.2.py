class Restaurant():
	"""Рестораны Минска"""

	def __init__(self, restaurant_name, cuisine_type, open_closed):
		"""Инициализирует атрибуты restaurant_name и cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.open_closed = open_closed

	def describe_restaurant(self):
		"""Выводит название ресторана и тип кухни"""
		print(f"\n{self.restaurant_name} has {self.cuisine_type} cuisine type.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is {self.open_closed} now.")

restaurant_1 = Restaurant("Teflis", "Georgian", "open")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Special Place", "Belarussian", "closed")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Saigon", "Vietnamese", "closed")
restaurant_3.describe_restaurant()
