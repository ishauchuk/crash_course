from employee import Employee

name = input('name: ')
surname = input('surname: ')
salary = int(input('salary: '))
increase = input('increase: ')

person = Employee(name, surname, salary).give_raise(increase)

