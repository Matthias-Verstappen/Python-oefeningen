# oefening 1.1

# Craane;Nathan;F013

with open('Files/classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        class_ind = record[2]
        print(class_ind)
        number_per_room = 0

        while line and record[2] == class_ind:
            print(f"\t{record[1]} {record[0]}")
            number_per_room += 1
            line = file.readline().rstrip()
            record = line.split(';')
        print(f'Number of students in classroom {class_ind} = {number_per_room}')