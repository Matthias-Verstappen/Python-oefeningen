# oefening 2.1

with open('Files/first_names.txt') as file:
    lines = file.readlines()
    lines.reverse()
    for line in lines:
        print(line, end='')