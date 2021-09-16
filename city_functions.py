
def country_city(country, city, population=''):
	"""Получаем страну и город"""

	if population:
		formatted_name = f'"{city.title()}, {country.title()} - population {population}"'
	else:
		formatted_name = f'"{city.title()}, {country.title()}"'
	return formatted_name