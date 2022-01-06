#oefening3

your_age = int(input("How old are you: "))
father_age = int(input("How old is your father: "))
count = 0

while father_age != 2 * your_age:
    count += 1
    your_age += 1
    father_age += 1

print("Within", count, "years, your father will have twice your age.",
      "\nYour father will be", father_age, "and you will be", your_age)