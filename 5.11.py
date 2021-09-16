list_numbers = []
for number in range(1, 11):
    list_numbers.append(number)
print(list_numbers)
for elem in list_numbers:
    if elem == 1:
        print('1st')
    elif elem == 2:
        print('2nd')
    else:
        print(f"{elem}th")