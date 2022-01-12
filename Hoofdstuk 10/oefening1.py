# oefening 1

tekst = input('Enter a text consisting only of letters and numbers: ')
numbers = set()
letters = set()

for character in tekst:
    if character in '0123465789':
        numbers.add(character)
    else:
        letters.add(character)

print('The numbers')
for number in numbers:
    print(number)
# print(*numbers)
print('The letters:')
for letter in letters:
    print(letter)
# print(*letters)