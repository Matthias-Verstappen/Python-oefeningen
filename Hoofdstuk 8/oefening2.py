# oefening 2

# Z25066;Application Development in Java;1ITF C;555274;Vannuffelen;Dries
with open('Files/courses.csv') as input_file:  # r = reading
    with open('Files/students.csv', 'w') as output_file:  # w = writing - a = appending
        line1 = input_file.readline().rstrip()  # kolomkoppen
        line = input_file.readline().rstrip()  # delete \n
        record = line.split(";")
        while line:  # zolang er records zijn
            student_indicative = record[3]  # criteria is studentennummer
            student_info = student_indicative + ";" + record[4] + ";" + record[5]
            while line and student_indicative == record[3]:  # zolang zelfde studentennummer
                student_info += ";" + record[1] + '(' + record[2] + ')'
                line = input_file.readline().rstrip()  # delete \n
                record = line.split(";")
            output_file.write(student_info + '\n')  # einde van student
            print(student_info)
