# Создание пустого списка для хранения прешельцев.
aliens = []

# Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Первые три пришельца превращаются из зеленых в красных.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print('.....')

# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")