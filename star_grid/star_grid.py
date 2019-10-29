import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from star import Star
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	sg_settings = Settings()	#'sg' for star_grid
	screen = pygame.display.set_mode(
		(sg_settings.screen_width, sg_settings.screen_height))
	pygame.display.set_caption("Star Grid")

	# Make a group of stars.
	stars = Group()

	# Create the grid of stars.
	gf.create_grid(sg_settings, screen, stars)

	while True: #Pygame requires an event loop or else it hangs.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		gf.update_screen(sg_settings, screen, stars)

run_game()
