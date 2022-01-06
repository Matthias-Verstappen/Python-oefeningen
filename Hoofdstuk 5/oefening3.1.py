#oefening 3.1

original = ["cat", "dog", "mouse", "rat", "squirrel", "owl", "rabbit"]
changed = []

for i in range(len(original)):
    changed.append(original[i])

for j in range(len(original)):
    changed[j - 1] = original[j]

print(original)
print(changed)

# for j in range(len(original)):
#     changed.insert(j - 1, original[j])        werkt ook maar is minder duidelijk
