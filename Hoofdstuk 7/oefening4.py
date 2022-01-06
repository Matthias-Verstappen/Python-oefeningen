#oefening 4

with open('Files/irish_song.txt') as song:
    line = song.readline()
    shortest = line.rstrip()
    while line != "":
        if len(line) < len(shortest):
            shortest = line.rstrip()
        line = song.readline()

print('The shortest line has {} characters'.format(len(shortest)))
print(f'{shortest}')