#oefening 8

boys = []
girls = []
with open('Files/contacts.csv') as file:
    line = file.readline() # stap 1 lezen
    while line: # stap 2 while
        record = line.split(';')    # stap 3 do sth
        if record[3].rstrip() == 'M':
            boys.append(record[1] + ' ' + record[0])
        else:
            girls.append(record[1] + ' ' + record[0])
        line = file.readline() # stap 4 opnieuw lezen

boys.sort()
girls.sort()
print(f'{len(girls)} girls:')
for item in girls:
    print(f"\t{item}")
print(f'{len(boys)} boys:')
for item in boys:
    print(f"\t{item}")