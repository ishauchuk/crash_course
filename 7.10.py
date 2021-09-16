responces = {}

polling_continue = True

while polling_continue:
    name = input("\nWhat's your name?\n")
    responce = input("\nWhat country would you like to visit in vacation?\n")

    responces[name] = responce

    new_name = input("\nWould like to get new answer from another person? (yes/no)\n")
    if new_name == 'no':
        polling_continue = False

print("\n--- Poll Results ---")
for name, country in responces.items():
    print(f"{name} is want to visit {country} in near future.")