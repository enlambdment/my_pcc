import pygame

def make_screen():
	"""Make an empty screen."""
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				print(event.key)

make_screen()