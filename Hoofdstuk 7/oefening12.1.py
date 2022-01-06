# oefening 12.1

import random
number = random.randint(1, 10)

with open(f'table_{number}.txt', 'w') as file:
    for i in range(1, 11):
        file.write(f'{i}x{number}={i * number}\n')