names = ['harry', 'bella', 'darie', 'ann', 'johnny', 'kate']

names_pooling = ['harry', 'darie', 'max']

for name in names:
    if name in names_pooling:
        print(f"\nThank you for voting in poll, {name.title()}.")
    else:
        print(f"\nWould you like to participate in voting, {name.title()}?")