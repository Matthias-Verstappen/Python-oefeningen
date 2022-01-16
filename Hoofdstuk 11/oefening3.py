# oefening 3

import numpy as np
from matplotlib import pyplot as plt

days = np.loadtxt(fname='Files/Temperatures.txt', delimiter=',', dtype=int, usecols=0)
temps = np.loadtxt(fname='Files/Temperatures.txt', delimiter=',', dtype=int, usecols=1)

plt.plot(temps)
plt.xticks(range(len(days)), days, rotation=90)

plt.title("Temperature measurements C°")
plt.xlabel('Days')
plt.ylabel('Temperatures')
# plt.legend()
plt.show()

# arr = np.genfromtxt(fname="Files/Temperatures.txt", delimiter=",")  # Get the values in an array
# print(arr)
#
# # tijd = arr[:, 0]  # days
# # temp = arr[:, 1]  # Temperatures
# plt.plot(arr[:, 1])
# plt.xticks(range(len(arr[:, 1])), arr[:, 0], rotation=90)
#
# plt.title("Temperatures")
# plt.xlabel("Days")
# plt.ylabel("Temperature")
#
# plt.show()