# oefening 5

number = int(input("Enter a number: "))
smallest = 10000000
biggest = 0
count = 0

if number == 0 and count == 0:
    print("No numbers entered.")
else:
    while number != 0:
        if number > biggest:
            biggest = number
            number = int(input("Enter a number: "))
            count += 1

        elif number < smallest:
            smallest = number
            number = int(input("Enter a number: "))
            count += 1


        else:
            number = int(input("Enter a number: "))
            count += 1

print("The difference between the largest number", biggest, "and the smallest", smallest, "=", biggest - smallest)
