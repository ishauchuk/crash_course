# file_path = 'c:\\Users\\ihar\\github\\test.py'

# with open(file_path) as file_object:
# 	contents = file_object.read()

# print(contents.rstrip())

filename = 'pi_digits.txt'
# filename = 'c:\\Users\\ihar\\github\\test.py'

with open(filename) as file_object:
	# for line in file_object:
	# 	print(line.rstrip())
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())