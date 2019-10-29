import matplotlib.pyplot as plt

five = list(range(1,6))
five_cubes = [x**3 for x in five]

plt.plot(five, five_cubes, linewidth=5)

# Set title & label axes.
plt.title("First Five Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
