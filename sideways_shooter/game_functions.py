import sys

import pygame
from bullet import Bullet 

def check_keydown_events(event, ss_settings, screen, ship, bullets):
	"""Respond to keypresses."""
	# This time, only keypresses K_UP & K_DOWN should apply.
	if event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ss_settings, screen, ship, bullets)

def fire_bullet(ss_settings, screen, ship, bullets):
	"""Fire a bullet if limit not reached yet."""
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < ss_settings.bullets_allowed:
		new_bullet = Bullet(ss_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	"""Respond to key releases."""
	if event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ss_settings, screen, ship, bullets):
	"""Respond to key events and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ss_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ss_settings, screen, ship, bullets):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ss_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

def update_bullets(bullets, screen):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()

	# Get rid of bullets that have disappeared.
	# This time, bullets disappear *over the right edge of the screen.*
	# In order to implement this, update_bullets requires 'screen' as
	# a parameter.
	# In turn, any places where update_bullets are called must pass 
	# a value to the 'screen' parameter.
	screen_rect = screen.get_rect()

	for bullet in bullets.copy():
		if bullet.rect.left >= screen_rect.right:
			bullets.remove(bullet)
	print(len(bullets))