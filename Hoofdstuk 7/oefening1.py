# oefening 1

with open('Files/first_names.txt') as file:
    line = file.readline()
    name_count = 0
    z_count = 0
    while line != "":
        if "z" in line.lower():
            z_count += 1
            name_count += 1
            line = file.readline()
        else:
            name_count += 1
            line = file.readline()

print(f'There are {name_count} first names in the file.')
print(f'{z_count} of which contain a "z".')