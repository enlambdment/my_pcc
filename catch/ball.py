import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
	"""A class to manage balls created & caught as gameplay progresses."""

	def __init__(self, c_settings, screen):
		"""
		Create a ball object at some random location, 
		along top of the screen. Make sure the ball
		image is entirely on the screen!
		"""
		super().__init__()
		self.screen = screen
		self.c_settings = c_settings

		# Need to load ball image & get its rect
		self.image = pygame.image.load(
			'images/tennisball.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# ... then calculate what part of screen is available
		available_x = self.screen_rect.width - self.rect.width

		# ... and create ball at random x-location along top of screen
		self.rect.x = randint(0, available_x)
		self.rect.y = 0

		# Store the ball's position as a decimal value.
		self.y = float(self.rect.y)

		self.speed_factor = c_settings.ball_speed_factor

	def update(self):
		"""Update the ball's position as it falls."""
		self.y += self.speed_factor
		self.rect.y = self.y

	def blitme(self):
		"""Draw the ball to the screen."""
		self.screen.blit(self.image, self.rect)


