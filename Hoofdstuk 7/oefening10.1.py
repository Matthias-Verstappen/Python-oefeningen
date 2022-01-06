# oefening 10.1

with open('hulpFile10.py') as input:
    line = input.readline()
    count = 1
    finished_line = ""
    while line:
        finished_line += f'{count} {line}\n'
        line = input.readline()
        count += 1
        print(line)

with open('output_oef10.txt', 'w', encoding='utf-8') as output:
    output.write(finished_line)