import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Make a random walk instance & fill in its trajectory.
	rw = RandomWalk(5000)		# use 5K points, instead of 50K default
	rw.fill_walk()

	point_numbers = list(range(rw.num_points))

	plt.plot(rw.x_values, rw.y_values, linewidth=2)

	plt.scatter(rw.x_values[0], rw.y_values[0], color='green', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], color='red', s=100)

	plt.show()

	# Ask if user wants a new plot
	keep_running = input("Make another random path? (y/n): ")
	if keep_running == 'n':
		break

