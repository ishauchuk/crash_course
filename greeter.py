# name = input("Please enter your name:\n")
# print(f"\nHello, {name}!")

# promt = "If you tell us who you are, we can personalize the messages you see."
# promt += "\nWhat is your first name? "

# name = input(promt)
# print(f"\nHello, {name}!")

# def greet_user(username):
#     """Выводит просто приветствие."""
#     print(f"Hello, {username.title()}!")

# greet_user('john')

def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Бесконечный цикл!
while True:
    print("\nPlease tell me your name:")
    print("(press 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")