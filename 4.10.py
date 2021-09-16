my_foods = ['pizza', 'falafel', 'carrot pie', 'sushi']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


print("\nThe first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are:")
print(my_foods[-3:])