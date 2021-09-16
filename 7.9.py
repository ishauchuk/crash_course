print("Sorry, we don't have pastrami")
sandwich_orders = ['hamburger',
                    'pastrami',
                    'chickenburger',
                    'pastrami',
                    'pastrami',
                    'crabsburger',
                    'cheeseburger']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)

print("I made:")
for burger in finished_sandwiches:
    print(f"\t{burger}")
