# oefening 7

tasks = {}
with open('Files/tasks.csv') as file:
    line = file.readline()  # column headings
    line = file.readline().rstrip()
# 9u;Esther;Jonas;Lotte;Lotte;Bert
    while line:
        record = line.split(';')
        for i in range(1, len(record)):  # from index 1 first names
            if record[i] in tasks:  # key=record[i]
                tasks[record[i]] += 1  # increase value   value= tasks[record[i]
            else:
                tasks[record[i]] = 1  # create new key/value pair
        line = file.readline().rstrip()

print('Task distribution:')
for person in tasks:
    print(person, tasks[person])  # print key, value

# sorting by key
for person in sorted(tasks):
    print(person, tasks[person])
