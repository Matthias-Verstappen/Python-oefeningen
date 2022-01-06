#oefening 6.1

word = input('Enter a string: ')
new_word = ''
# print(word[3:])

while len(word) >= 3:
    new_word = new_word + word[1:3]
    new_word = new_word + word[0]
    word = word[3:]
new_word = new_word + word
print(new_word)