guest_list = ['Avicii', 'Kurt Kobein', 'Victor Tsoy']
for guest_number in range(len(guest_list)):
	print(f"Hello my friend {guest_list[guest_number]}. I'm glad to see you.")
print('*' * 10)
print(f"{guest_list[1]} doesn`t comes.")
print('*' * 10)
guest_list[1] = 'Amy Winehouse'
for guest_number in range(len(guest_list)):
	print(f"Hello my friend {guest_list[guest_number]}. I'm glad to see you.")
print('*' * 10)
print("I have new seats. List of guests will be changed.")
guest_list.insert(0, 'Michael Jackson')
guest_list.insert(2, 'Freddy Mercury')
guest_list.append('Igor Talkov')
print('*' * 10)
for guest_number in range(len(guest_list)):
	print(f"Hello my friend {guest_list[guest_number]}. I'm glad to see you.")
print('*' * 10)
print('Sorry, but only 2 persons will be come to dinner.')
for guest_number in range(len(guest_list) - 2):
	print(f'Sorry, {guest_list.pop()}, dinner is canceled.')
print('*' * 10)
for guest_number in range(len(guest_list)):
	print(f"Hello my friend {guest_list[guest_number]}. Dinner will be tommorow.")
print('*' * 10)
for guest_number in range(len(guest_list)):
	del guest_list[0]
print(guest_list)