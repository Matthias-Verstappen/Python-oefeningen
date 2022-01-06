#oefening 3

original_list = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
print(original_list)
for i in range(0, len(original_list) - 1):
    original_list[i - 1] = original_list[i]
print(original_list)