#oefening 6

# lap = "top"
# print(lap[1:] + lap[:1])

woord = str(input("Enter a word: "))
length = len(woord)

while length >= 3:
    print(woord[1:3] + woord[:1], end="")
    woord = woord[3:]
    length = len(woord)
print(woord[::])
