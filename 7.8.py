sandwich_orders = ['hamburger', 'chickenburger', 'crabsburger', 'cheeseburger']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich}.")
    finished_sandwiches.append(finished_sandwich)
print("I made:")
for burger in finished_sandwiches:
    print(f"\t{burger}")
