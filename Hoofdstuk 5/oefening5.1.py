#oefening 5.1

# array = [0, 42, 18, 17, 0, 2, 19, 10, 5, 14]
# array = [42, 18, 0, 37, 2, 19, 10, 5, 14]
array = [42, 18, 17, 0, 2, 19, 0]
print(array)
for i in range(len(array) - 1):
    if array[i] == 0:
        biggest_odd = 0
        for j in range(i, len(array) - 1):
            if array[j] % 2 != 0 and array[j] > biggest_odd:
                biggest_odd = array[j]
        array[i] = biggest_odd
print(array)