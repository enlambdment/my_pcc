import pygame

class Rocket():	#should be just like ship, except with all 4 directions

	def __init__(self, r_settings, screen):
		"""Initialize the ship and set its starting position."""
		self.r_settings = r_settings
		self.screen = screen

		# Load the rocket image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the *center* of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

		# Store a decimal value for the ship's center.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		# Movement flags, to allow continuous motion
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the rocket's position based on movement flags."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.r_settings.rocket_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.r_settings.rocket_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.r_settings.rocket_speed_factor
		if self.moving_up and self.rect.top > 0:
			self.centery -= self.r_settings.rocket_speed_factor

		self.rect.centerx = self.centerx
		self.rect.centery = self.centery

	def blitme(self):
		"""Draw the rocket at its current location."""
		self.screen.blit(self.image, self.rect)
