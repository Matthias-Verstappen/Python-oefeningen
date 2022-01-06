#oefening 12

from random import randint

number = randint(1, 10)
with open(f'table_{number}.txt', 'w') as file:
    for i in range(1, 11): # range tot 10
        file.write(f"{i} * {number} = {i * number}\n")