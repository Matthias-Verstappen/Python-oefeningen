#oefening 2.1

number = int(input("Enter a number: "))
zeros = 0
sixes = 0

while number > 0:
    if number % 10 == 0:
        zeros += 1
        number //= 10
    elif number % 6 == 0:
        sixes += 1
        number //= 10
    else:
        number //= 10
print(f'The number consists of {zeros} zeros and {sixes} sixes.')