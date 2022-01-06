#oefening 3.1

first = int(input("Number 1: "))
second = int(input("Number 2: "))
third = int(input("Number 3: "))
smallest = first

if second < smallest:
    smallest = second
elif third < smallest:
    smallest = third
print(f'The smallest number is {smallest}')