#oefening 1.1

color = input('What is your favorite color: ')

print(color[0], color[2])
print('This color consists of', len(color), 'letters')
print()

for i in range(0, len(color)):
    print(color[i], "=", ord(color[i]))

print()

for j in range(0, len(color)):
    if (j + 1) % 2 == 0:
        print("**" + color[j] + "**")
    else:
        print('#' + color[j] + '#')