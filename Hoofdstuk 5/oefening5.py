#oefening 5

my_list = [0, 42, 18, 21, 17, 0, 2, 19, 0, 10, 5, 0, 8, 14]


for i in range(len(my_list) - 1):
    if my_list[i] == 0:
        current_max_odd = 0
        for j in range(i, len(my_list) - 1):
            if my_list[j] % 2 != 0 and my_list[j] > current_max_odd:
                current_max_odd = my_list[j]
                my_list[i] = current_max_odd
print(my_list)
