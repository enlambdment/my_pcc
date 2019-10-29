def make_album(artist_name, album_title, tracks_num=''):
	"""Builds a dictionary consisting of an album."""
	if tracks_num:
		album = {'artist_name': artist_name, 'album_title': album_title, 'tracks_num': tracks_num}
	else:
		album = {'artist_name': artist_name, 'album_title': album_title}
	return album


