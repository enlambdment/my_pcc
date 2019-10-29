import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from drop import Drop
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	rd_settings = Settings()	#'rd' for raindrop
	screen = pygame.display.set_mode(
		(rd_settings.screen_width, rd_settings.screen_height))
	pygame.display.set_caption("Raindrops")

	# Make a group of raindrops.
	drops = Group()

	# Create the grid of raindrops.
	gf.create_grid(rd_settings, screen, drops)

	while True: #Pygame requires an event loop or else it hangs.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		gf.update_drops(drops)
		gf.swap_drops(drops)
		# print(len(drops))	# There were 121 drops upon starting. 
							# Not all of them were visible -
							# fixed this in get_number_rows()
		gf.update_screen(rd_settings, screen, drops)

run_game()