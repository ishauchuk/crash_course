responces = {}

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя
    name = input("\nWhat is your name? ")
    responce = input("Which mountain would you like to climb? ")

    # Ответ хранится в словаре
    responces[name] = responce

    # Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, responce in responces.items():
    print(f"{name} would like to climb {responce}.")