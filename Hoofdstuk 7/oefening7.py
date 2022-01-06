# oefening 7

with open('Files/playlist.txt', encoding='UTF8') as playlist:
    songs = playlist.readlines()
    songs = sorted(songs)
    print('Playlist', end="\n")
    for song in songs:
        song_data = song.split(";")
        print(song_data[0] + "\t" + str(song_data[1]).upper(), '(' + str(song_data[2]).lower().rstrip() + ')')
