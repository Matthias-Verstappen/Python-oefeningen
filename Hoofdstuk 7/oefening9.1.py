#  oefening 9.1

# 1/08/2018 0:00;20.32;2.75;745;61.45;0

with open('Files/weather_2018 08.csv') as file:
    line = file.readline().rstrip()
    line = file.readline().rstrip()
    highest = 0
    while line:
        record = line.split(';')
        if float(record[1]) > float(highest):
            highest = record[1]
        line = file.readline().rstrip()
print(f'The highest temperature in this period = {highest} °C.')