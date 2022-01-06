#oefening 8.1

digit = int(input('What final digit do you want to check the numbers on: '))

count = 1
end_digit_count = 0

while count != 10:
    number = int(input('Enter a number: '))
    count += 1
    if number % 10 == digit:
        end_digit_count += 1
print(f'{end_digit_count} out of 10 numbers end on 7')