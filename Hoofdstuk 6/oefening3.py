#oefening 3


def print_square(number, character):
    line = number * character
    for i in range(number):
        print(line)
    # number_copy = number
    # while number_copy >= 1:
    #     print(character * number)
    #     number_copy -= 1


input_character = input("Which character must be used to form the lines (enter = stop): ")
while input_character != "":
    input_size = int(input("Number of characters per line = number of lines = "))
    print_square(input_size, input_character)
    input_character = input("Which character must be used to form the lines (enter = stop): ")

