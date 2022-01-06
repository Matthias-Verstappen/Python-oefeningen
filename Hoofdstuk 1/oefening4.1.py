#oefening 4.1

first = input("Enter the first name: ")
second = input("Enter the second name: ")

print(f'Before changing: {first} {second}')
hulp = first
first = second
second = hulp
print(f'After changing: {first} {second}')