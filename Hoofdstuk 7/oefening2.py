#oefening 2

with open('Files/first_names.txt') as file:
    lines = file.readlines()
    lines.reverse()
    print(*lines)