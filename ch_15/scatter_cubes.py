import matplotlib.pyplot as plt

n = 5000

x_values = list(range(1,n+1))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
	edgecolor='none', s=40)

# Set title and label chart axes
plt.title("Graph of Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set tick label size.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()