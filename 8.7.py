def make_album(executor, name_album, number_tracks=None):
    music_album = {executor: name_album}
    if number_tracks:
        music_album['number tracks'] = number_tracks
    return music_album

print(make_album('avicii', 'True'))
print(make_album('rammstein', 'Paris', 18))
print(make_album('linkin park', 'meteora'))