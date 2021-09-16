
filename_1 = 'cats.txt'
filename_2 = 'dogs.txt'

filenames = [filename_1, filename_2]

for i in filenames:
	try:
		with open(i, encoding='utf-8') as file_object:
			contents = file_object.read()
		print(contents)
	except FileNotFoundError:
		pass
	print("*"*15)