# oefening 4.1

with open('Files/irish_song.txt') as file:
    line = file.readline().rstrip()
    shortest = line
    while line:
        if len(line) < len(shortest):
            shortest = line
        line = file.readline().rstrip()
    print(f'The shortest line has {len(shortest)} characters.')
    print(shortest)
