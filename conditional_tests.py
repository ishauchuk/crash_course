line_1 = 'Python'
line_2 = 'Java'
line_3 = 'python'

if line_1 == line_2:
    print('True')
else:
    print('False')

if line_3 == line_1.lower():
    print('True')
else:
    print('False')

if line_1 >= line_2:
    print('True')
else:
    print('False')

if line_3 == line_1.lower() and not line_1 == line_2:
    print('True')
else:
    print('False')

if 'y' in line_1 and not 'a' in line_3:
    print('True')
else:
    print('False')