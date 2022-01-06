# oefening 3.1

# datum;temperatuur;PAR;zonlicht;RV;neerslag
# 8/10/2018 0:00;7.58;3.28;0;84.78;0µ

print('Average temperatures:')
with open('Files/weather_2018 10.csv') as file:
    line = file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        date_ind = record[0].split(' ')[0]
        count = 0
        total = float(0)
        while line and date_ind == record[0].split(' ')[0]:
            total += float(record[1])
            line = file.readline().rstrip()
            record = line.split(';')
            count += 1
        average = total / count
        print(f'{date_ind}\tnumber of measurements = {count}\taverage = {average}')
    print('>'*60)