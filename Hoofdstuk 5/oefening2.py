#oefening 2

original_list = [9, 17, 25, 4, 12, 7]
new_list = []

for i in original_list:
    if i % 2 == 0:
        new_list.insert(0, i)
    else:
        new_list.append(i)
print(new_list)