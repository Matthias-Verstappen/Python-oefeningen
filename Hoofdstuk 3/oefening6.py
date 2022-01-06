# oefening 6

number = int(input("Enter a number: "))
stringabc = ""

for i in range(number, -1, -1):
    stringabc = stringabc + str(i) + " ... "
print(stringabc)
