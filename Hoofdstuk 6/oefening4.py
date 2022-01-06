# oefening 4
import random
from itertools import groupby


# def all_equal(iterable):
#     g = groupby(iterable)
#     return next(g, True) and not next(g, False)


def generate_list(length, lower_limit=1, upper_limit=6):
    array = []
    for i in range(length):
        array.append(random.randint(lower_limit, upper_limit))
    return array


def filter(array):
    hulp = []
    for i in array:
        if i not in hulp:
            hulp.append(i)
    array = hulp
    return array


# dice_amount = int(input("How many dice do you want to roll? "))
# result_throw = generate_list(dice_amount, 1, 6)
# filtered_result = filter(result_throw)
# print(f'You threw: {result_throw}')
# print(f'Your unique rolls were: {filtered_result}')

def poker(dice_amount=5):
    array = generate_list(dice_amount)
    count = 0
    while len(filter(array)) != 1:
        count += 1
        array = generate_list(dice_amount)
        print(f'You threw: {array}')
    print(f'You threw Poker after {count} times.')


# def poker(dice_amount=5):
#     array = generate_list(dice_amount)
#     count = 0
#     while all_equal(array) is False:
#         count += 1
#         array = generate_list(dice_amount)
#         print(f'You threw: {array}')
#     print(f'You threw Poker after {count} times.')


poker()