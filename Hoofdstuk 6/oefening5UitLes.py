# oefening 5 volgens docent

# functions
def count(text):  # text= "Life of Brian"
    result = [0, 0]  # list met index [0] voor hoofdletters en [1] voor kleine letters
    for item in text:
        if item.isupper():
            result[0] += 1  # hoofdletters
        elif item.islower():
            result[1] += 1  # kleine letters
    return result


# ---------------------------------------------------------------------------------------

#  main program

# answer = input('Your string: ')
# result_count = count(answer)
# print(f'Number of capitals = {result_count[0]}\n'
#       f'Number of lowercase letters = {result_count[1]}')

# stap 1
password = input('Set your password (at least 2 uppercase and 3 lowercase letters) : ')
password_count = count(password)

# stap 2 & 3
while password_count[0] < 2 and password_count[1] < 3:
    # stap 4
    password = input('Set your password (at least 2 uppercase and 3 lowercase letters) : ')
    password_count = count(password)
