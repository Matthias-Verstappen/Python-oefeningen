#oefening 3

with open('Files/first_names.txt') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if i % 10 == 0 and i != 0:
            print()
        print(lines[i].rstrip().ljust(13), end="\t")