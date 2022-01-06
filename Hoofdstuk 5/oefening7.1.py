#oefening 7.1

original = [2, 4, 5, 9]
new = []

i = 0
while i < 2 * len(original) - 1:
    new.append(0)
    i += 1
new.append(original[-1])
print(original)
print(new)