from make_album import make_album

while True:
	print("Enter artist name, album title, & optional tracks number: ")
	print("\n(Type q to quit at any time) ")

	art_n = input("Artist name: ")
	if art_n == 'q':
		break

	alb_t = input("Album title: ")
	if alb_t == 'q':
		break

	trk_n = input("Tracks number (optional): ")
	if trk_n == 'q':
		break

	alb = make_album(art_n, alb_t, trk_n)
	print(alb)