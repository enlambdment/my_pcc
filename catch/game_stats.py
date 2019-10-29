class GameStats():
	"""Track statistics for Catch."""

	def __init__(self, c_settings):
		"""Initialize statistics."""
		self.c_settings = c_settings
		self.reset_stats()

		# Start Catch in an active state.
		self.game_active = True

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.misses_left = self.c_settings.ball_limit