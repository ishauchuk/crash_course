cities = ['Minsk', 'Zakopane', 'Berlin', 'Paris', 'Barcelona', 'Riga']
cities_upper = []
for elem in range(len(cities)):
	cities_upper.append(cities[elem].upper())
print('\t', cities_upper)
print('*' * 10)
print(cities_upper[0].title())
print('*' * 10)
cities[-1] = 'Rigas'
print(cities)
cities.append('Vienna')
print(cities)
cities.insert(-1, 'Budapest')
print(cities)
print(sorted(cities))
print(cities)
cities.reverse()
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)