class Settings():
	"""A class to store all settings for Rocket."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Rocket settings
		self.rocket_speed_factor = 1.5