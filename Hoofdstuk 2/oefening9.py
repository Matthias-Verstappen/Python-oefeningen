#oefening 9
number_1 = int(input("Number 1 (0, 1 or 2): "))
number_2 = int(input("Number 2 (0, 1 or 2): "))
number_3 = int(input("Number 3 (0, 1 or 2): "))

if number_1 == number_2 and number_2 == number_3 and number_1 == 2:
    print("10")
elif number_1 == number_2 and number_2 == number_3 and number_1 != 2:
    print("5")
elif number_2 == number_3 and number_1 != number_2:
    print("1")
else:
    print("0")
