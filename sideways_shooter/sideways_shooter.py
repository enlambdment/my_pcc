import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	ss_settings = Settings()
	screen = pygame.display.set_mode(
		(ss_settings.screen_width, ss_settings.screen_height))
	pygame.display.set_caption("Sideways Shooter")

	# Make a ship.
	ship = Ship(ss_settings, screen)
	# Make a group to store bullets in.
	bullets = Group()

	# Start the main loop for the game.
	while True:
		gf.check_events(ss_settings, screen, ship, bullets)
		ship.update()			#calls update method on each pass thru loop
		gf.update_bullets(bullets, screen)
		gf.update_screen(ss_settings, screen, ship, bullets)

run_game()