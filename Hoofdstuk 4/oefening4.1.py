#oefening 4.1

word = input('Enter a word: ')

if len(word) % 2 == 0:
    middle = int(len(word) / 2)
    if word[:middle] == word[:middle - 1:-1]:
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')
elif len(word) % 2 != 0:
    middle = len(word) // 2
    if word[:middle] == word[:middle:-1]:
        print(f'{word} is a palindrome.')
    else:
        print(f'{word} is not a palindrome.')