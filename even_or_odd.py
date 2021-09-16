while  True:
    number = int(input("Enter a number, and I'll tell you if it's even or odd:\n"))
    if number == 0:
        print("Alarm!")
    elif number % 2 == 0:
        print(f"\nThe mumber {number} is even.")
    else:
        print(f"\nThe number {number} is odd.")