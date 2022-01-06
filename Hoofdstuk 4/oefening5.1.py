#oefening 5.1

text = input('Enter a text: ')
count = 0
for i in range(2, len(text)):
    if text[i] == text[i - 1] == text[i - 2]:
        count += 1
if count == 0:
    print('There are no triples in this text.')
elif count == 1:
    print('There is one triple in this text.')
else:
    print(f'There are {count} triples in this text.')