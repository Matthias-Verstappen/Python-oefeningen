#oefening 1.1
count = 0
product = 1
number = int(input("Enter a number, stop by entering a zero: "))
while number != 0:
    product = product * number
    count += 1
    number = int(input("Enter a number, stop by entering a zero: "))
print(f'The product of the {count} numbers is {product}')