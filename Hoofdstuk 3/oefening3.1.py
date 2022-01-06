#oefening 3.1

you = int(input('How old are you: '))
father = int(input('How old is your father: '))

count = 0
while father != 2 * you:
    father += 1
    you += 1
    count += 1


print(f'Within {count} years your father will have twice your age\n'
      f'Your father will be {father} and you will be {you}')