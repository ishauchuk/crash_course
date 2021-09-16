while True:
    requested_topping = input("Enter your topping:\n")
    if requested_topping == 'quit':
        break
    else:
        print(f"Adding {requested_topping} to your order.")
        