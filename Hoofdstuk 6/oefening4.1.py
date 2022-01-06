# oefening 4.1
import random


def generate_list(length, lower_limit=1, upper_limit=6):
    array = []
    i = 0
    while i < length:
        array.append(random.randint(lower_limit, upper_limit))
        i += 1
    return array

def filter(list):
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])
    return new_list


# dice = int(input('How many dice do you want to roll? '))
# roll = generate_list(dice)
# print(f'You threw {roll}')
# print(f'Your unique rolls were: {filter(roll)}')

count = 1
roll = generate_list(5)
while len(filter(roll)) != 1:
    print(f'You threw: {roll}')
    count += 1
    roll = generate_list(5)

print(f'You threw: {roll}')
print(f'You threw poker after {count} times')