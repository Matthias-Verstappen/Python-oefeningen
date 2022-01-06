# oefening 13

with open('Files/hamlet.txt') as input_file:
    with open('Files/hamlet2.txt', 'w') as output_file:
        lines = input_file.readlines()  # inlezen lijst
        for item in lines:  # loop doorheen lijst
            for character in ',.;:?!':  # karakter komt voor
                item = item.replace(character + '  ', character + ' ')  # replace 2 spaties -> 1 spatie
            output_file.write(item)
