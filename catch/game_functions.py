import sys
from time import sleep

import pygame
from ball import Ball

# no need to import Catcher because there is no 
# game function that involve create / deleting / 
# updating catchers

def check_keydown_events(event, c_settings, screen, catcher):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		catcher.moving_right = True
	elif event.key == pygame.K_LEFT:
		catcher.moving_left = True
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, catcher):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		catcher.moving_right = False
	elif event.key == pygame.K_LEFT:
		catcher.moving_left = False

def check_events(c_settings, screen, catcher):
	"""Respond to key events and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, c_settings, screen, catcher)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, catcher)

def update_screen(c_settings, screen, catchers, balls):
	"""Update images on the screen and flip to the new screen."""
	# Redraw all bullets *behind* ship and aliens.
	screen.fill(c_settings.bg_color)

	for ball in balls.sprites():
		balls.draw(screen)

	for catcher in catchers:
		catcher.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def update_catcher(c_settings, screen, catchers, balls):
	"""
	Update position of catcher, and get rid of any caught or disappeared balls.
	"""
	for catcher in catchers:
		catcher.update()

	# # From now on, instead of deleting balls that hit the bottom
	# # of the screen, we'll track these in game stats.
	# for ball in balls.copy():
	# 	if ball.rect.top >= c_settings.screen_height:
	# 		balls.remove(ball)

	check_ball_catcher_collisions(c_settings, screen, catchers, balls)

def check_ball_catcher_collisions(c_settings, screen, catchers, balls):
	"""Respond to ball-catcher collisions."""
	collisions = pygame.sprite.groupcollide(balls, catchers, True, False)

	if len(balls) == 0:
		# Create a new ball to replace the ball just deleted.
		new_ball = Ball(c_settings, screen)
		balls.add(new_ball)

def ball_missed(c_settings, stats, screen, balls):
	"""Respond to missing a ball."""

	if stats.misses_left > 1:	#off-by-1 error in text
		# Decrement misses left.
		stats.misses_left -= 1

		# Pause.
		sleep(0.5)

	else: # no misses left - game over.
		stats.game_active = False

def check_balls_missed(c_settings, stats, screen, balls):
	"""Check if any balls have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	for ball in balls.sprites():
		if ball.rect.bottom >= screen_rect.bottom:
			# Replace ball back at the top, so it doesn't
			# endlessly trip off this condition.
			balls.empty()
			new_ball = Ball(c_settings, screen)
			balls.add(new_ball)
			# Call ball_missed in order to update stats.
			ball_missed(c_settings, stats, screen, balls)

def update_balls(c_settings, stats, screen, balls):
	"""Update the position of all currently existing balls."""
	balls.update()

	# Look for missed balls, i.e. balls 
	check_balls_missed(c_settings, stats, screen, balls)
