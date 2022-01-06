# r0851784
# Verstappen Matthias
# 1ITF11

import random


def get_dividers(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)
    return result


def list_to_string(list):
    return " ".join(str(item) for item in list)


# main

number = random.randint(1, 1000)
list_dividers = get_dividers(number)
list_as_string = list_to_string(list_dividers)
count = 1
print(f'We have calculated dividers for {number}.')

attempt = int(input(f'Attempt {count}: '))
while count != 5 and attempt not in list_dividers:
    count += 1
    attempt = int(input(f'Attempt {count}: '))

if attempt in list_dividers and count == 1:
    print(f'You needed {count} attempt to find a correct divider.')
    print(f'The dividers for {number} are {list_as_string}')
elif attempt in list_dividers and count != 1:
    print(f'You needed {count} attempts to find a correct divider.')
    print(f'The dividers for {number} are {list_as_string}')
else:
    print(f'You did not find a divider.')
    print(f'The dividers for {number} are {list_as_string}')
