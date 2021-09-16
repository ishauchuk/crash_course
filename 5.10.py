current_users = ['Anie', 'Darie', 'Masha', 'Glasha', 'Alex']
new_users = ['KIM', 'DARIE', 'John', 'Glasha', 'Victor']
current_users_lower = []
new_users_lower = []

for name in current_users:
	current_users_lower.append(name.lower())
print(current_users_lower)

for name in new_users:
	for new_lower in current_users_lower:
	    if elem in current_users:
	    	print(f"User with name {name} is exists. Choose another name.")
	else:
	    print(f"{name} is free for registration.")