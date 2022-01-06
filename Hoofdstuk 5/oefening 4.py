# oefening 4

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
number = 4

if number in my_tuple:
    final_index = len(my_tuple) - my_tuple[::-1].index(number)
    new_tuple = my_tuple[final_index:]
    print(my_tuple)
    print(new_tuple)
else:
    print(f"The number {number} doesn't appear in this tuple.")
