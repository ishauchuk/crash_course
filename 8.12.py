
def sandwitch_components(*ingredients):
    for ingredient in ingredients:
        print(ingredient)

sandwitch_components('salat', 'cheese', 'chicken')
print('*' * 10)
sandwitch_components('bread', 'ketchup', 'cutlet')
print('*' * 10)
sandwitch_components('tomato', 'cucumber', 'chicken', 'bread')