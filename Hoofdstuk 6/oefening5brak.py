# oefening 5

def count_uppercase(text):
    count = 0
    for i in text:
        if i == i.upper():
            count += 1
    return count


def count_lowercase(text):
    count = 0
    for i in text:
        if i == i.lower():
            count += 1
    return count


def count_upper_and_lower(text):
    text = text.split(" ")
    text = "".join(text)
    array = [0] * 2          # kan ook als array = [0, 0]
    array[0] = count_uppercase(text)
    array[1] = count_lowercase(text)
    return array


# text = input("Your string: ")
# array_count = count_upper_and_lower(text)
# number_capitals = array_count[0]
# number_lower = array_count[1]
#
# print(f'Number of capitals: {number_capitals}')
# print(f'Number of lowercase letters: {number_lower}')

def set_password():
    password = input("Set you password (at least 2 uppercase and 3 lowercase letters): ")
    array_count = count_upper_and_lower(password)
    number_capitals = array_count[0]
    number_lower = array_count[1]
    while number_capitals < 2 or number_lower < 3:
        password = input("Set you password (at least 2 uppercase and 3 lowercase letters): ")
        array_count = count_upper_and_lower(password)
        number_capitals = array_count[0]
        number_lower = array_count[1]

set_password()
