
filename = 'learning_python.txt'

with open(filename) as file_object_1:
	contents_1 = file_object_1.read()
print(contents_1)

print("*"*40)

with open(filename) as file_object_2:
	for line in file_object_2:
		print(line.rstrip())

print("*"*40)

with open(filename) as file_object_3:
	lines = file_object_3.readlines()

for line in lines:
	print(line.rstrip())