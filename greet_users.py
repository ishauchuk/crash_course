def greet_users(names):
    """Вывод проостого приветствия для каждого юзера"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['john', 'darie', 'alexandro']
greet_users(usernames)
print(usernames)