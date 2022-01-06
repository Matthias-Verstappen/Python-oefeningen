#oefening 2
count_zero = 0
count_six = 0
number = int(input("Enter a number: "))

while number > 0:
    if number % 10 == 0:
        count_zero += 1
        number //= 10
    elif number % 10 == 6:
        count_six += 1
        number //= 10
print("The number consists of", count_zero, "zeros and", count_six, "sixes")
