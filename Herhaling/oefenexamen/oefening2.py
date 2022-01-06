# Matthias Verstappen
# r0851784
# 1 ITF 11# functions


# adres = input('Your address is: ')

def letters(adres):
    count = 0
    fifth_letters = []
    for i in range(len(adres)): # for i in range(0, len(adres), 5)
        if (count == 0 or count % 5 == 0) and adres[i] != " ": # if adres[i] not in fifth_letters:
            fifth_letters.append(adres[i].lower())
            count += 1 #mag dan weg
        else: #mag dan weg
            count += 1 #mag dan weg
    return fifth_letters


#main

adres = input('Your address is: ')
letters_list = letters(adres)
game_title = 'Letter guessing game:'
print(f'Every 5th letter substracted from the address (without blanks) is:\n {letters_list} ')

print()
print(game_title)
print("-" * len(game_title))

while len(letters_list) != 0:
    guess = input(f'Still {len(letters_list)} to go: ')
    if guess in letters_list:
        letters_list.remove(guess)
print('Yes, you did it!')


#Kleinhoefstraat 4 Geel