class Settings():
	"""A class to store all settings for Catch."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (240, 100, 100)

		# Catcher settings
		self.catcher_speed_factor = 2

		# Ball settings
		self.ball_speed_factor = 2.5
		self.ball_limit = 3
