rivers_countries = {
                    'nile': 'egypt',
                    'volga': 'russia',
                    'pripyat': 'ukraine',
                    }
for river, country in rivers_countries.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")
print('*' * 10)
for river in rivers_countries.keys():
    print(river.title())
print('*' * 10)
for country in rivers_countries.values():
    print(country.title())