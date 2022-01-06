#oefening 7.1

first_number = int(input('First number: '))
second_number = int(input('Second number: '))

if first_number < 0:
    first_number *= -1
elif second_number < 0:
    second_number *= -1

if first_number == second_number:
    print(0)
elif first_number % 5 == 0 and second_number % 5 == 0:
    if first_number > second_number:
        print(second_number)
    else:
        print(first_number)
elif first_number > second_number:
    print(first_number)
else:
    print(second_number)