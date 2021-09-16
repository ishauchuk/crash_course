pet_1 = {
        'owner': 'Borya',
        'type': 'cat',
        'nickname': 'Barsik',
        }

pet_2 = {
        'owner': 'Vasya',
        'type': 'dog',
        'nickname': 'Bobik',
        }

pet_3 = {
        'owner': 'Irene',
        'type': 'hamster',
        'nickname': 'Homa',
        }

pets = [pet_1, pet_2, pet_3]

animal_list = []

for pet in pets:
    for value in pet.values():
        animal_list.append(value)

for i in range(0, 9, 3):
    print(f"{animal_list[i]} has {animal_list[i + 1]} with nickname \
{animal_list[i+2]}.")
