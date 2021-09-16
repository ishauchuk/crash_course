
from random import choice

list_of_choise = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
					'a', 'b', 'c', 'd', 'e')

lucky_ticket = []
my_ticket = [7, 2, 'e', 'a']
print(my_ticket)

tick = 0
while True:
	for elem in range(4):
		iter_symbol = choice(list_of_choise)
		lucky_ticket.append(iter_symbol)
	tick += 1
	if lucky_ticket == my_ticket:
		print(f"Win! You need {tick} attempts to get succes!")
		print(lucky_ticket)
		break
	else:
		print('Sorry, next time you win')
		print(lucky_ticket)
	print(f"It was {tick} attempt")
	lucky_ticket.clear()

