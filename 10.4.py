
filename = 'guest_book.txt'

while True:
	name = input('Introduce yourself:\n')
	if name:	
		with open(filename, 'a') as file_object:
			file_object.write(f"Your name is {name}. I added you.\n")
	else:
		break