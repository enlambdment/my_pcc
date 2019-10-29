import sys

import pygame
from drop import Drop

# def update_screen(rd_settings, screen, drops):
# 	"""Update raindrops on the screen and flip to the new screen."""
# 	screen.fill(rd_settings.bg_color)
# 	drops.draw(screen)

# 	# Make the most recently drawn screen visible.
# 	pygame.display.flip()

def update_drops(drops):
	"""
	Update position of drops. 
	Then, if any drops fall off the screen,
	replace the fallen row with a new row
	in the grid.
	"""
	drops.update()

	# # testing check_bottom() method
	# for drop in drops:
	# 	print(drop.check_bottom())

def update_screen(rd_settings, screen, drops):
	"""Update images on the screen and flip to the new screen."""
	screen.fill(rd_settings.bg_color)
	drops.draw(screen)

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def get_number_drops_x(rd_settings, drop_width):
	"""Determine the number of drops that fit in a row."""
	available_space_x = rd_settings.screen_width - 2 * drop_width
	number_drops_x = int(available_space_x / (2 * drop_width))
	return number_drops_x

def get_number_rows(rd_settings, drop_height):
	"""Determine the number of rows of stars that fit on the screen."""
	available_space_y = rd_settings.screen_width - 2 * drop_height
	number_rows = int(available_space_y / (2 * drop_height)) - 3
		# don't create any raindrops in the initial grid that will
		# be invisible upon initializing program!
	return number_rows

def create_drop(rd_settings, screen, drops, drop_number, row_number):
	"""
	Create a drop, then set its position in a grid
	based upon drop # and row # parameters. Then, 
	add the drop to the drop-group.
	"""
	drop = Drop(rd_settings, screen)
	drop_width = drop.rect.width
	drop_height = drop.rect.height

	# Calculate drop positions
	drop.rect.x = drop_width + 2 * drop_width * drop_number
	drop.rect.y = drop_height + 2 * drop_height * row_number
	drops.add(drop)

def create_grid(rd_settings, screen, drops):
	"""Create a full grid of drops."""
	drop = Drop(rd_settings, screen)
	number_drops_x = get_number_drops_x(rd_settings, drop.rect.width)
	number_rows = get_number_rows(rd_settings, drop.rect.height)

	# Create the grid of drops.
	for row_number in range(number_rows):
		for drop_number in range(number_drops_x):
			create_drop(rd_settings, screen, drops, drop_number,
				row_number)

def replace_drop(drop, drops):
	"""
	Replaces a drop about to be deleted with one positioned to replace it,
	in the top row.
	"""
	drop_number = int(((drop.rect.x / drop.rect.width) - 1) / 2)

	# new row's drops should all start at y = 0, top of screen
	create_drop(drop.rd_settings, drop.screen, drops, drop_number, -1/2)	

def swap_drops(drops):
	"""
	Iterates over the drops Group to identify drops that fell off the screen,
	copy them back to the top row, then remove them.
	"""
	for drop in drops.copy():
		if drop.check_bottom():
			replace_drop(drop, drops)
			drops.remove(drop)