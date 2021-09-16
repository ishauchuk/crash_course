guest_list = ['Avicii', 'Kurt Kobein', 'Victor Tsoy']
for guest_number in range(3):
	print(f"Hello my friend {guest_list[guest_number]}. I'm glad to see you.")
print(f"{guest_list[1]} doesn`t comes.")
guest_list[1] = 'Amy Winehouse'
for guest_number in range(3):
	print(f"Hello my friend {guest_list[guest_number]}. I'm glad to see you.")
