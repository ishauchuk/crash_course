def make_album(executor, name_album, number_tracks=None):
    music_album = {executor: name_album}
    if number_tracks:
        music_album['number of tracks'] = number_tracks
    return music_album

while True:
    print("\n(press 'q' at any time to quit)")
    exe = input("\nPlease tell me your executor: ")
    if exe == 'q':
        break

    print("(press 'q' at any time to quit)")
    n_album = input("\nPlease tell me name of album: ")
    if n_album == 'q':
        break

    print("(press 'q' at any time to quit)")
    n_tracks = input("\nPlease tell me number of tracks: ")
    if n_tracks == 'q':
        break
    elif n_tracks == '':
        n_tracks=None
    else:
        n_tracks = int(n_tracks)

    print('\n', make_album(exe, n_album, n_tracks))