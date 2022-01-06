#oefening 4
number_1 = int(input('Number 1: '))
number_2 = int(input('Number 2: '))
number_3 = int(input('Number 3: '))
sum_1 = number_1 + number_2
sum_2 = number_1 + number_3
sum_3 = number_2 + number_3

if sum_1 == number_3:
    print("This works")
elif sum_2 == number_2:
    print("This works")
elif sum_3 == number_1:
    print("This works")
else:
    print("This won't work.")