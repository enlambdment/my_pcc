import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Make a random walk, and plot the points.
	rw = RandomWalk()
	rw.fill_walk()

	# Set the size of the plotting window.
	plt.figure(figsize=(10, 6))

	point_numbers = list(range(rw.num_points))

	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=20)

	# Mark the starting dot green.
	plt.scatter(rw.x_values[0], rw.y_values[0], c='green', s=100)

	# Mark the ending dot red.
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another random walk? (y/n): ")
	if keep_running == 'n':
		break