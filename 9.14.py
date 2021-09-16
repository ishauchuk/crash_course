
from random import choice

list_of_choise = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
					'a', 'b', 'c', 'd', 'e')
lucky_ticket = []

for elem in range(4):
	iter_symbol = choice(list_of_choise)
	lucky_ticket.append(iter_symbol)

full = []
for i in lucky_ticket:
	full += str(i)


print(lucky_ticket)
