import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
	"""A class to represent a single drop in the grid."""

	def __init__(self, rd_settings, screen):
		"""Initialize the drop and set its starting position."""
		super().__init__()
		self.screen = screen
		self.rd_settings = rd_settings

		# Load the drop image and set its rect attribute.
		self.image = pygame.image.load(
			'images/raindrop.png')
		self.rect = self.image.get_rect()

		# Start each new drop near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def blitme(self):
		"""Draw the drop at its current location."""
		self.screen.blit(self.image, self.rect)

	def update(self):
		"""Move the drop down."""
		self.rect.y += self.rd_settings.drop_fall_speed

	def check_bottom(self):
		"""Check whether the drop has fallen off the screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.y > screen_rect.bottom:
			return True
		else:
			return False 