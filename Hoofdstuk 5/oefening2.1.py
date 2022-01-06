#oefening 2.1

# array = [9, 17, 25, 4, 12, 7]
array = [23, 12, 54, 85, 46, 30, 26, 64, 91]

for i in range(len(array)):
    if array[i] % 2 == 0:
        array.insert(0, array[i])
        array.pop(i + 1)
print(array)
