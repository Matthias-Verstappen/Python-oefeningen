# extra oefening 2

count = 0

getal = input("Press Enter for each new striker you see\n"
              "If you want to pass a group, enter the number of strikers\n"
              "If you want to stop, type S and press enter ")

while getal != "S":
    if getal == "":
        count += 1
    else:
        count = count + int(getal)
    getal = input()

quit = str(input("Do you really want to stop Y/N? "))

if quit == "Y" or quit == "y":
    print(f"Total number of strikers = {count}")
elif quit == "N" or quit == "n":
    while getal != "S":
        if getal == "":
            count += 1
        else:
            count = count + getal
        getal = input()


# niet stoppen nog uitwerken, met boolean eventueel