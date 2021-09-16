# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
    
# print(pets)

# def describe_pet(animal_type, pet_name):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'homa')
# describe_pet('cat', 'tom')

def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')
describe_pet(pet_name='homa', animal_type='hamster')