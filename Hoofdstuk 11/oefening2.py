# oefening 2

import numpy as np

grades_linux = np.genfromtxt(fname='Files/points_linux.csv', delimiter=';', dtype=int, filling_values=0)
grades_networks = np.genfromtxt(fname='Files/points_networks.csv', delimiter=';', dtype=int, filling_values=0)
grades_python = np.genfromtxt(fname='Files/points_python.txt', delimiter=';', dtype=int, filling_values=0)
grades_web = np.genfromtxt(fname='Files/points_web.txt', delimiter=';', dtype=int, filling_values=0)

all_grades = np.array([grades_linux, grades_networks, grades_python, grades_web])
total_grades = all_grades.mean(0)
grades_percentages = total_grades[:, 1] / 20 * 100      # moet eigenlijk anders

title = "November 2021 Exam Results:"
print(title)
print("-" * len(title))
print(f'The highest score this exam period is: {max(grades_percentages)}%')
print(f'The lowest score this exam period is: {min(grades_percentages)}%')



# print(grades_percentages)

# print(grades_linux)
# print(grades_networks)
# print(grades_python)
# print(grades_web)