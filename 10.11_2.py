import json

filename = 'number.json'

with open(filename) as f:
	number = json.load(f)

print(f"I know your favorite number! It is '{number}'.")