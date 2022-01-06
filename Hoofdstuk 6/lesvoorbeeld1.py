# functies
# import math
# import random
# print(math.pi, math.sqrt(4), math.ceil(9.4))
# print(random.randint(1, 38))

def print_double(value):
    print(value * 2)


def multiply(value):
    return value * 4


def printing(number1="+", number2=5):
    print(number1 * number2)


def using_lists(numbers_list):
    numbers_list.reverse()
    return numbers_list


# main programma -> functies oproepen
printing()        #zonder parameters -> kan door default parameters
printing(4, 5)
printing("@")

# numbers = [1, 2, 3, 4, 5, 6]
# print(using_lists(numbers))

# print_double(8)
# print_double("jow")

# print(multiply(2))
# print(multiply("bla"))

# printing("makke",5)
# printing([1,2,3,7,8,5,6], 3)
