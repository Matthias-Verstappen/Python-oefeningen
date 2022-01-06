# oefening 4.1

original = (1, 2, 3, 4, 5, 6, 7, 8)
number = 4

if number in original:
    final_index = original[::-1].index(number)
    new_tuple = original[final_index:]
    print(original)
    print(new_tuple)
else:
    print('The number 4 does not appear in this tuple')

