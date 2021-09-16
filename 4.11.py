pizza_names = ['margarita', 'four seasons', 'chicken blue cheese']
for pizza in pizza_names:
	print(f"I like {pizza} pizza")
print("\nI really love pizza!")

friend_pizza = pizza_names[:]
print('******')
print(friend_pizza)
pizza_names.append('carbonara')
friend_pizza.append('peperoni')
print("\nMy favorite pizzas are:")
for pizza in pizza_names:
	print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
	print(pizza.title())