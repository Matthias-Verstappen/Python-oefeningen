# oefening 3

# tijdstip;temperatuur;PAR;zonlicht;RV;neerslag
# 8/10/2018 0:00;7.58;3.28;0;84.78;0

print('Average temperatures:')
with open('Files/weather_2018 10.csv') as file:
    line1 = file.readline().rstrip()
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        date_indicative = record[0].split(' ')[0]  # datum weerhouden zonder tijd
        date_number = 0
        date_total = 0
        while line and date_indicative == record[0].split(' ')[0]:
            date_number += 1
            date_total += float(record[1])  # rekenen -> string omzetten naar float
            line = file.readline().rstrip()
            record = line.split(';')
        average = date_total / date_number  # einde van elke datum -> bereken gemiddelde
        print(date_indicative + '\tnumber of measurements = ' + str(date_number) + '\t average = ',
              '{:.4}'.format(average))
    print('>' * 60)  # einde van programma
