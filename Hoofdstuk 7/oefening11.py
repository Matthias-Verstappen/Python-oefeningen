#oefening 11

with open('output.txt') as input:
    with open('notNumbered.txt', 'w') as output:
        line = input.readline()
        adjusted_line = ""
        count = 1
        while line:
            line = line[1:]
            adjusted_line = f"{line}\t"
            output.write(adjusted_line)
            count += 1
            line = input.readline()
            print(adjusted_line)

#     output.write(adjusted_line)
