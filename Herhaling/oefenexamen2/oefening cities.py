# oefening cities

import numpy as np
import matplotlib.pyplot as plt

cities = []
population = []

with open('city_population.txt') as file:
    line1 = file.readline()  # kolomkoppen stap 1
    line = file.readline().rstrip()
    while line:  # stap 2
        record = line.split('#')  # stap 3
        cities.append(record[0])
        population.append(int(record[1]))  # opletten -> nood aan integers om te rekenen
        line = file.readline().rstrip()  # stap 4

# with numpy array
population_array = np.array(population)

# plt.figure(figsize=(10, 10))
# plt.pie(population_array, labels=cities, autopct='%1.1f%%', startangle=-40, wedgeprops=dict(width=0.5))
# plt.title('Population per city\n' + 'Sum: ' + str(population_array.sum()))
# plt.show()

plt.figure(figsize=(10, 5))
plt.bar(cities, population_array, label='Population')
plt.title('Population per city')
plt.xlabel('City')
plt.ylabel('Population')
plt.show()