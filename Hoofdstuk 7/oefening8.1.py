#  oefening 8.1

# Anthoni;Erwin;erwinanthoni@itfactory.com;M
girls = []
boys = []

with open('Files/contacts.csv') as file:
    lines = file.readlines()
    for line in lines:
        record = line.split(";")
        if record[3].rstrip() == "M":
            boys.append(record[1] + ' ' + record[0])
        else:
            girls.append((record[1] + ' ' + record[0]))

girls.sort()
boys.sort()
print(f'{len(girls)} girls:')
for girl in girls:
    print('\t' + girl)
print(f'{len(boys)} boys:')
for boy in boys:
    print('\t' + boy)
