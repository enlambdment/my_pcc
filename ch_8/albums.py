from make_album import make_album as mk 

a1 = mk('Forn', 'The Departure of Consciousness')
print a1

a2 = mk('Forn', 'Weltschmerz', 4)
print a2

a3 = mk('Triumvir Foul', 'Spiritual Bloodshed')
print a3

a4 = mk(album_title='Revisionist', artist_name='Sannhet')
print a4

a5 = mk(tracks_num=3, album_title='Signals III', artist_name='Sabled Sun')
print a5