#oefening 4
import random

number = random.randint(1, 25)
guess = int(input("Enter a positive number: "))
count = 0

while number != guess:
    if guess < number:
        count += 1
        print("Higher!")
        guess = int(input("Enter a positive number: "))

    elif guess > number:
        count += 1
        print("Lower!")
        guess = int(input("Enter a positive number: "))
count += 1
print("You have guessed the number", number, "in", count, "turns.")