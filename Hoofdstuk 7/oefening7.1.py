# oefening 7.1

# 12:59;Ace Of Base;THE SIGN

print('Playlist')
with open('Files/playlist.txt', encoding='UTF-8') as file:
    lines = file.readlines()
    lines.sort()
    for line in lines:
        record = line.split(';')
        print(record[0], '\t', record[1].upper(), f'({record[2].lower().rstrip()})')
        line = file.readline().rstrip()
