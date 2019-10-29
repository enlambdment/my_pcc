import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from catcher import Catcher
from ball import Ball
import game_functions as gf

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	c_settings = Settings()
	screen = pygame.display.set_mode(
		(c_settings.screen_width, c_settings.screen_height))
	pygame.display.set_caption("Catch")

	# Create an instance to store game stats.
	stats = GameStats(c_settings)

	# Make a catcher and a ball.
	# The ball will be kept track of inside a group,
	# so that we can use pygame collisions method on it.
	# In order for this to work, catcher must belong 
	# inside a group of as well (even though we never
	# replace it.)

	balls = Group()
	catchers = Group()

	# Create the initial ball
	ball = Ball(c_settings, screen)
	balls.add(ball)

	# and the catcher.
	catcher = Catcher(c_settings, screen)
	catchers.add(catcher)

	# Start the main loop for the game.
	while True:
		for catcher in catchers:
			gf.check_events(c_settings, screen, catcher)

		# just as bullet positions are updated, *then*
		# all collisions checked, inside a function call
		# before updating the screen, something similar 
		# should happen inside an 'update_bullets' call

		# pass update_catcher the group containing the
		# sole catcher, since update_catcher will cal
		# a function using groupcollisions()

		if stats.game_active:
			gf.update_catcher(c_settings, screen, catchers, balls)
			gf.update_balls(c_settings, stats, screen, balls)
		
		gf.update_screen(c_settings, screen, catchers, balls)

run_game()