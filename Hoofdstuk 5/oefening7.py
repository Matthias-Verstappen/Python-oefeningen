#oefening 7

list1 = [2, 4, 5, 9, 8, 21]
list2 = []

i = 0
while i < len(list1) * 2:
    list2.append(0)
    i += 1

list2[-1] = list1[-1]
print(len(list2))
print(list2)