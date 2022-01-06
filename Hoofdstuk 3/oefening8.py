#oefening 8

digit = int(input("What final digits do you want to check the numbers on: "))
count = 0
teller = 0
while teller != 10:
    teller += 1
    number = int(input("Enter a number: "))
    if number % 10 == digit:
        count += 1

print(count, "out of 10 numbers end on", digit)
