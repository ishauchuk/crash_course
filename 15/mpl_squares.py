import matplotlib.pyplot as plt

input_values = range(1, 5001)
squres = [x**2 for x in input_values]
cubes = [x**3 for x in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Blues, s=10)
ax.plot(input_values, squres, linewidth=3)
ax.plot(input_values, cubes, linewidth=3)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square and cube numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square and Cube of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)

plt.show()