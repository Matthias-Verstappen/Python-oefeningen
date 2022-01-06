# oefening 1.1

with open('Files/first_names.txt') as file:
    line = file.readline().rstrip()
    count = 0
    count_z = 0
    while line:
        count += 1
        if 'z' in line.lower():
            print(line)
            count_z += 1
        line = file.readline().rstrip()
    print(f'There are {count} names in the file.')
    print(f'{count_z} of which contain a letter z.')
