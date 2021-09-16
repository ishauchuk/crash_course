class Restaurant():
	"""Рестораны Минска"""

	def __init__(self, restaurant_name, cuisine_type, open_closed):
		"""Инициализирует атрибуты restaurant_name и cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.open_closed = open_closed

	def describe_restaurant(self):
		"""Выводит название ресторана и тип кухни"""
		print(f"{self.restaurant_name} has {self.cuisine_type} cuisine type.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is {self.open_closed} now.")

restaurant = Restaurant("Teflis", "Georgian", "open")
print(restaurant.restaurant_name, restaurant.open_closed)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
