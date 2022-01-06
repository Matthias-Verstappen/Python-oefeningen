# lesvoorbeeld

import numpy as np

loaded_data = np.loadtxt(fname='Files/student_grades_3.csv', delimiter=';', dtype=int,
                         skiprows=1)  # inlezen in 2d array
# print(loaded_data)

max_grades = np.max(loaded_data, axis=0)  # verticaal
print(max_grades)
min_grades = np.min(loaded_data, axis=0)  # horizontaal
print(min_grades)
mean_grades = np.mean(loaded_data, axis=0)  # gemiddelde
print(mean_grades)
print('Grades analysis Python:')
print('max', max_grades[0], 'min', min_grades[0], 'mean', mean_grades[0])
print('Grades analysis Linux:')
print('max', max_grades[1], 'min', min_grades[1], 'mean', mean_grades[1])
print('Grades analysis R&S:')
print('max', max_grades[2], 'min', min_grades[2], 'mean', mean_grades[2])