name_list = ['Anie', 'Darie', 'Masha', 'Glasha', 'admin']

if name_list:
	for name in name_list:
	    if name == 'admin':
	        print(f"Hello, {name}, would you like to see a status report?")
	    else:
	        print(f"Hello, {name}, thanl you  for loggin in again.")
else:
	print('We need to add some users!!')