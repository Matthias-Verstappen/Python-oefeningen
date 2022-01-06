# oefening 6

import numpy as np
from matplotlib import pyplot as plt

loaded_data = np.loadtxt(fname='Files/student_grades_3.csv', delimiter=';', dtype=int,
                         skiprows=1)  # inlezen in 2d array

plt.title('Grades analysis Python')
plt.hist(loaded_data[:, 0], bins=len(loaded_data[:, 0]), facecolor='green')
# eerste kolom van array, bins = 20 (20 cijfers van python)
plt.xlabel('Python grades out of 20')
plt.ylabel('Amount of grades out of 20')
plt.xticks(range(21))  # range van 0 tem 20
plt.yticks(range(7))  # range van 0 tem 6
plt.show()
