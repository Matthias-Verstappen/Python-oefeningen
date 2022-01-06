# refresher exercise
# functions
def fill_list():
    playlist = []
    for i in range(5):
        playlist.append(input('Song ' + str(i + 1) + ': '))
    return playlist


def menu():
    print("\ta - Overview\n\tb - Define longest title\n\tc - 5 letters in a row\n"
          "\td - No vowels\n\te - Cutting the playlist\n\ts - Stop")
    selection = input("\tMake a selection: ").lower()
    return selection


def print_overview(playlist):
    print("Playlist:")
    for i in range(len(playlist)):
        print(str(i + 1), playlist[i])


def longest_title(playlist):
    longest = playlist[0]
    for i in range(len(playlist)):
        if len(playlist[i]) > len(longest):
            longest = playlist[i]
    return longest


def title_per_5_letters(playlist):
    getal = valid_input(playlist)
    title = playlist[getal - 1]
    for i in range(len(title)):
        if i > 1 and i % 5 == 0:
            print(title[i], end="\n")
        else:
            print(title[i], end=" ")
    print()


def no_vowels(song):
    vowels = ["a", "e", "u", "i", "o"]
    adjusted_title = ""
    for i in range(len(song)):
        if song[i] not in vowels:
            adjusted_title = adjusted_title + song[i]
        elif song[i] in vowels:
            adjusted_title = adjusted_title + " "
    return adjusted_title


def valid_input(playlist):
    number = int(input(f'Enter the number of the song max {len(songs)}: '))
    while number not in range(1, len(playlist) + 1):
        number = int(input(f'Enter the number of the song max {len(songs)}: '))
    return number


# -------------------------------------------------------------
# main program

# songs = ["Blinding Lights", "Dance Monkey", "Sweet but Psycho", "Imagine Dragons", "Mirrors"]  # test array

songs = fill_list()
keuze = menu()
while keuze != 's':
    if keuze == 'a':
        print_overview(songs)
        keuze = menu()
    elif keuze == 'b':
        print(f'The longest title "{longest_title(songs)}" has {len(longest_title(songs))} characters.')
        keuze = menu()
    elif keuze == 'c':
        title_per_5_letters(songs)
        keuze = menu()
    elif keuze == 'd':
        choice = valid_input(songs)
        print(no_vowels(songs[choice - 1]))
        keuze = menu()
    elif keuze == 'e':
        choice = valid_input(songs)
        new_playlist = songs[choice - 1:]
        print(new_playlist)
        keuze = menu()

        # C ZONDER FUNCTION
        # number = int(input(f"Enter the number of the song max {len(songs)}: ")) # stap 1
        # while number not in range(1, len(songs) + 1): # stap 2 en 3
        #     number = int(input(f"Enter the number of the song max {len(songs)}: "))
        # song = songs[number - 1]
        # for i in range(len(song)):
        #     if i % 5 == 0:
        #         print()
        #     print(song[i], end=" ")
        # print()
        #
        # # stap 4
        # keuze = menu()
