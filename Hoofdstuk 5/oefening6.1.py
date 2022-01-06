#oefening 6.1

text = input('Enter a text: ')
array = []

for i in range(len(text)):
    if text[i] != " " and text[i] not in array:
        array.append(text[i])
array = sorted(array)

print(array)

for j in range(len(array)):
    print(array[j], end=" ")

print()

for j in range(len(array)):
    print(array[j], end="\t")
