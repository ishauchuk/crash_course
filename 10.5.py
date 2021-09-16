
filename = 'opinion.txt'

while True:
	opinion = input("Why you like programming?\n")
	if opinion:	
		with open(filename, 'a') as file_object:
			file_object.write(opinion + '\n')
	else:
		break