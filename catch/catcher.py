import pygame
from pygame.sprite import Sprite

class Catcher(Sprite):

	def __init__(self, c_settings, screen):
		"""Initialize the catching character and set its starting position."""
		super().__init__()
		self.screen = screen
		self.c_settings = c_settings

		# Load the catcher iamge and get its rect.
		self.image = pygame.image.load(
			'images/happy_orange.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start the catcher at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		# Movement flags, to allow continuous motion
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the catcher's position based on movement flags."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.c_settings.catcher_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.c_settings.catcher_speed_factor

		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
