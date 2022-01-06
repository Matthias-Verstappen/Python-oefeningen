# oefening 4.1
import random

number = random.randint(1, 21)
count = 0

guess = int(input('Enter a number between 1 and 21: '))
while guess != number:
    if guess < number:
        print('Higher!')
        count += 1
        guess = int(input('Enter a number between 1 and 21: '))
    elif guess > number:
        print('Lower!')
        count += 1
        guess = int(input('Enter a number between 1 and 21: '))
count += 1
print(f'You have guessed the number {number} in {count} turns.')