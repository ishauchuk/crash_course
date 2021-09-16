def make_pizza(size, *topings):
    """Выводит описание пиццы."""
    print(f"\nMaking a {size}-inch pizza with the following topings:")
    for toping in topings:
        print(f"- {toping}")
