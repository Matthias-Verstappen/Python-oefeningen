# oefening 3.1

with open('Files/local_booking.txt') as file:
    line = file.readline().rstrip()
    rooms = set()
    while line:
        record = line.split(';')
        rooms.add(record[3])
        line = file.readline().rstrip()
print('Classrooms')
for room in rooms:
    print(room)