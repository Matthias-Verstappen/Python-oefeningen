# oefening 2.1

# Z25066;Application Development in Java;1ITF C;555274;Vannuffelen;Dries

with open('Files/courses.csv') as file:
    line = file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        studentind = record[3]
        student = f"{record[3]};{record[4]};{record[5]}"
        while line and studentind == record[3]:
            student = student + f';{record[1]} ({record[2]})'
            line = file.readline().rstrip()
            record = line.split(';')
        # print(student)
        with open('students.csv', 'a') as output:
            output.write(student + '\n')

