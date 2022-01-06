#oefening 6

import random

getal = random.randint(1, 10)

with open(f'Files/wish{getal}.txt') as file:
    line = file.readline()
    print(f'Wish {getal}', end='\n')
    print()
    while line:
        if line != "\n":
            line = line.rstrip()
            print(line)
        line = file.readline()