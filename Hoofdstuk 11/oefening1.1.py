# oefening 1.1

import numpy as np

loaded_data = np.loadtxt(fname='Files/student_grades_3.csv', delimiter=';', dtype=int, skiprows=1)

max_grades = loaded_data.max(0)
min_grades =loaded_data.min(0)
mean_grades = loaded_data.mean(0)

print(f'Grades analysis Python:')
print(f'max {max_grades[0]}\tmin {min_grades[0]}\tmean {mean_grades[0]}')
print(f'Grades analysis Linux:')
print(f'max {max_grades[1]}\tmin {min_grades[1]}\tmean {mean_grades[1]}')
print(f'Grades analysis Routing & Switching:')
print(f'max {max_grades[2]}\tmin {min_grades[2]}\tmean {mean_grades[2]}')

# print(type(loaded_data))
# print(loaded_data)