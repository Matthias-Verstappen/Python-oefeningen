# oefening 1.1

original = ['cat', 'dog', 'mouse', 'rat', 'squirrel', 'owl', 'rabbit']

changed = []
for i in range(len(original)):
    changed.append(original[i])

changed[0] = original[-1]
changed[-1] = original[0]


print('original list:\t', original)
print('After the switch:\t', changed)
