# oefening 3

# maandag, september 18, 2017;10:15;11:45;P216C;APPLICATIEONTWIKKELING IN C;

with open('Files/local_booking.txt') as file:
    classrooms = set()  # create empty set + add()
    line = file.readline().rstrip()  # lege lijn weghalen stap 1
    while line:  # stap 2
        record = line.split(';')  # stap 3
        classrooms.add(record[3])  # klaslokaal
        line = file.readline().rstrip()  # opnieuw inlezen

print('Classrooms:')
for item in classrooms:
    print(item)
