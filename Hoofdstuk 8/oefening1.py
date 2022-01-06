# oefening 1

with open('Files/classrooms.txt') as file:
    # Craane;Nathan;F013
    line = file.readline().rstrip()
    record = line.split(";")
    while line:
        classroom = record[2]
        print(classroom)
        count = 0
        while line and classroom == record[2]:
            print(f"\t{record[1]} {record[0]}")
            count += 1
            line = file.readline().rstrip()
            record = line.split(";")
        print(f'Number of students in the classroom {classroom} = {count}')
