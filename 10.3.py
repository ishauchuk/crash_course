
filename = 'guest.txt'

name = input('Enter your name:\n')

with open(filename, 'a') as file_object:
	file_object.write(f"Your name is {name}.\n")