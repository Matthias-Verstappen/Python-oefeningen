#oefening 4.1

first = int(input("Number 1: "))
second = int(input("Number 2: "))
third = int(input("Number 3: "))

if first + second == third or second + third == first or first + third == second:
    print('This works')
else:
    print("This won't work")