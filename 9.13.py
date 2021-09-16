from random import randint


class Die():
 	"""Random cube choise"""

 	def __init__(self, sides=6):
 		"""Create cube with some sides"""
 		self.sides = sides

 	def roll_die(self):
 		"""Rolling """
 		number = randint(1, self.sides)
 		print(f"Number of side is {number}")


list_of_choise = [6, 10, 20]

for elem in list_of_choise:
	cube = Die(elem)
	for elem in range(10):
		cube.roll_die()