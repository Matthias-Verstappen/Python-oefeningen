#oefening 10

with open('hulpFile10.py') as read:
    line = read.readline()
    count = 1
    finished_line = ""
    while line:
        finished_line += f'{count} {line}\n'
        line = read.readline()
        count += 1
        print(line)

with open('output.txt', 'w', encoding='UTF-8') as output:
    output.write(finished_line)