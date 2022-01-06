# r0851784
# Verstappen Matthias
# 1ITF11

slice_index = None
result = ""
count = 0

word = input('Enter a word: ')
while word != "-1":
    character = input('Enter a character until which you would like to show your word: ')
    if character in word:
        slice_index = word.find(character)
        result = word[:slice_index]
        count = len(word[slice_index:])
    else:
        result = word
        count = 0

    if count > 1:
        print(f'Result: {result}')
        print(f'{count} characters have been removed.')
    elif count == 0:
        print(f'Result: {result}')
        print(f'No characters have been removed.')
    elif count == 1:
        print(f'Result: {result}')
        print(f'{count} character has been removed.')
    word = input('Enter a word: ')


