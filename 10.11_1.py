import json

filename = 'number.json'
number = int(input('What is your favorite number? '))
with open(filename, 'w') as f:
	json.dump(number, f)