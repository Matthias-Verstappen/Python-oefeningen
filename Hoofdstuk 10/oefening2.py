# oefening 2

with open('Files/first_names1ITF.txt', encoding='utf-8') as itf1:
    with open('Files/first_names2ITF.txt', encoding='utf-8') as itf2:
        names1 = set()
        names2 = set()

        line1 = itf1.readline().rstrip()
        line2 = itf2.readline().rstrip()
        while line1:
            names1.add(line1)
            line1 = itf1.readline().rstrip()
        while line2:
            names2.add(line2)
            line2 = itf2.readline().rstrip()

double_names = names1.intersection(names2)
print(f'In 1ITF there are {len(names1)} different first names.')
print(f'In 1ITF there are {len(names2)} different first names.')
print(f'These are the {len(double_names)} names appearing in 1ITF and 2ITF.')
for name in sorted(double_names):
    print(name)
