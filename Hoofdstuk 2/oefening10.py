#oefening 10
first_number = int(input("First number: "))
second_number = int(input("Second number: "))
numbers = [65, 72, 83, 90]

if 30 <= first_number <= 40 or first_number in numbers and 30 <= second_number <= 40 or second_number in numbers:
    print("Both numbers are ok.")
else:
    print("They are not ok.")