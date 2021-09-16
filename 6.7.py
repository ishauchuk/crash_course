# human = {'first_name': 'Alex', 'last_name': 'Duh', 'age': 29, 'city': 'Minsk'}
# print("first name", human['first_name'])
# print("last name", human['last_name'])
# print("age", human['age'])
# print("city", human['city'])

human_1 = {'first_name': 'Alex', 
            'last_name': 'Duh', 
            'age': 29, 
            'city': 'Minsk',
            }
human_2 = {'first_name': 'Ihar', 
            'last_name': 'Shauchuk', 
            'age': 29, 
            'city': 'Minsk',
            }
human_3 = {'first_name': 'Serg', 
            'last_name': 'Charnukha', 
            'age': 28, 
            'city': 'Pryzhany',
            }

people = [human_1, human_2, human_3]

for human in people:
    print(f"Name: {human['first_name']}")
    print(f"\tFull name: {human['first_name']} {human['last_name']}")
    print(f"\tLocation and age: {human['city']}, {human['age']} years")