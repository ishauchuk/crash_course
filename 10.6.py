
print("\nGive me two numbers. You will get summ")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("You cant't enter anything except digits!")
	else:
		print(answer)