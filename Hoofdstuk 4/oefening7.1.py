#oefening 7.1

woord = input('Enter a text: ')
langste = 1
count = 1
for i in range(1, len(woord) - 1):
    if woord[i] == woord[i - 1]:
        count += 1
        if count > langste:
            langste = count
    else:
        count = 1
print(f'The length of the largest block in this text is {langste}')