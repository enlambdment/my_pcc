import sys

import pygame
from star import Star

from random import randint

def update_screen(sg_settings, screen, stars):
	"""Update stars on the screen and flip to the new screen."""
	screen.fill(sg_settings.bg_color)
	stars.draw(screen)

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def get_number_stars_x(sg_settings, star_width):
	"""Determine the number of stars that fit in a row."""
	available_space_x = sg_settings.screen_width - 2 * star_width
	number_stars_x = int(available_space_x / (2 * star_width))
	return number_stars_x

def get_number_rows(sg_settings, star_height):
	"""Determine the number of rows of stars that fit on the screen."""
	available_space_y = sg_settings.screen_height - 2 * star_height
	number_rows = int(available_space_y / (2 * star_height))
	return number_rows

def create_star(sg_settings, screen, stars, star_number, row_number):
	"""Create an alien and place it in the row."""
	star = Star(sg_settings, screen)
	star_width = star.rect.width
	star_height = star.rect.height

	# To get a more realistic grid, adjust each star's position by a random amount.
	rand_x = randint(-20, 20)
	rand_y = randint(-20, 20)

	# Update star positions with random offset.
	star.rect.x = star_width + 2 * star_width * star_number + rand_x
	star.rect.y = star_height + 2 * star_height * row_number + rand_y
	stars.add(star)

def create_grid(sg_settings, screen, stars):
	"""Create a full grid of stars."""
	star = Star(sg_settings, screen)
	number_stars_x = get_number_stars_x(sg_settings, star.rect.width)
	number_rows = get_number_rows(sg_settings, star.rect.height)

	# Create the grid of stars.
	for row_number in range(number_rows):
		for star_number in range(number_stars_x):
			create_star(sg_settings, screen, stars, star_number, 
				row_number)