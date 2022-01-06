# oefening 7

tekst = str(input("Enter a text: "))
max_length = 1
temporary_max = 1

for i in range(0, len(tekst) - 1):
    if tekst[i] == tekst[i + 1]:
        temporary_max += 1
    else:
        temporary_max = 1
    if temporary_max > max_length:
        max_length = temporary_max
print(f"The length of the largest block in this text is {max_length}")
