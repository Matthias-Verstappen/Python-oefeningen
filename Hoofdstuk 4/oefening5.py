# oefening 5

tekst = str(input("Enter a text: "))
counter = 0

for i in range(0, len(tekst) - 1):
    if tekst[i:i+3] == tekst[i] * 3:
        counter += 1

if counter == 0:
    print("There are no triples in this text.")
elif counter == 1:
    print("There is one triple in this text.")
else:
    print(f"There are {counter} triples in this text.")