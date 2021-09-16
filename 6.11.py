cities = {
        'Minsk': {
            'country': 'Belarus',
            'population': '2 million',
            'fact': '1067',
        },

        'Moscow': {
            'country': 'Russia',
            'population': '12 million',
            'fact': '1147',
        },

        'Warsaw': {
            'country': 'Poland',
            'population': '1.8 million',
            'fact': '1300',
        },
}

for city, city_info in cities.items():
    print(f"{city} is located in {city_info['country']} \
and has population {city_info['population']} people. \
\n{city} was founded in {city_info['fact']} year.\n")