#oefening 9

with open('Files/weather_2018 08.csv') as file:
    line = file.readline()
    line = file.readline()
    heetste = -1000
    while line:
        if line != "\n":
            weather_info = line.split(";")
            temperatuur = weather_info[1]
            if float(temperatuur) > float(heetste):
                heetste = temperatuur
        line = file.readline()
print(f'The highest temperature in this period = {heetste} °C')