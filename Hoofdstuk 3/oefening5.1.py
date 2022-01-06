#oefening 5.1

smallest = 999999
largest = 0

number = int(input('Enter a number: '))
while number != 0:
    if number < smallest:
        smallest = number
        number = int(input('Enter a number: '))
    elif number > largest:
        largest = number
        number = int(input('Enter a number: '))
    else:
        number = int(input('Enter a number: '))
difference = largest - smallest
print(f'The difference between the largest number {largest} and the smallest number {smallest} = {difference}')