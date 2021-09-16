class Restaurant():
	"""Рестораны Минска"""

	def __init__(self, restaurant_name, cuisine_type, \
		open_closed, number_served=0):
		"""Инициализирует атрибуты restaurant_name и cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.open_closed = open_closed
		self.number_served = 0

	def describe_restaurant(self):
		"""Выводит название ресторана и тип кухни"""
		print(f"{self.restaurant_name} has {self.cuisine_type} cuisine type.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is {self.open_closed} now.")

	def set_number_served(self, number_served):
		self.number_served = number_served
		print(f"The number seved visitors is {self.number_served}.")

	def increment_number_served(self, number):
		self.number = number
		self.number_served += number

restaurant = Restaurant("Teflis", "Georgian", "open")
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 7
print(restaurant.number_served)
restaurant.set_number_served(9)
restaurant.increment_number_served(15)
print("Today restaurant has been visited", restaurant.number_served, "people.")
# restaurant.set_number_served()
