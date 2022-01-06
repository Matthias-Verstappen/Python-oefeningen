#oefening 1

original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]

saved_first = original_list[0]
original_list[0] = original_list[-1]
original_list[-1] = saved_first

print(original_list)