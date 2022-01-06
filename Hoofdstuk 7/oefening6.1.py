# oefening 6.1

import random

number = random.randint(1, 10)
print(f'Wish {number}')
with open(f'Files/wish{number}.txt') as file:
    line = file.readline().rstrip()
    while line:
        print(line)
        line = file.readline().rstrip()

