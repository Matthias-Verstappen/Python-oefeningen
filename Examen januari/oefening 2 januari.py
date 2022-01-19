# r0851784
# Verstappen Matthias
# 1ITF11

import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

xmlDoc = ET.parse('grades.xml')
root = xmlDoc.getroot()

print('These courses are available:\n')
count = 1
names = []
academic_years = []
average_scores = []

for courses in root.iter('course'):
    name = courses[0].text
    names.append(name)
    years = []
    average_scores_year = []
    for course in courses:
        for year in course.iter('year'):
            years.append(year.get('aj'))
            total_score_year = 0
            count_results = 0

            for score in year.iter('result'):
                total_score_year += int(score.text)
                count_results += 1
            average_scores_year.append(total_score_year / count_results)
    average_scores.append(average_scores_year)
    academic_years.append(years)


for name in names:
    print(f'{(names.index(name) + 1)}: {name}')
print()
choice = input('Please enter the number of a course: ')

print(f"The selected course is {names[int(choice) - 1]}")
print()
print(f'{academic_years[int(choice) - 1]}')  # years
print(f'{average_scores[int(choice) - 1]}')  # scores


years = academic_years[int(choice) - 1]
scores = average_scores[int(choice) - 1]

plt.title(f'{names[int(choice) - 1]}')
plt.bar(years, scores, facecolor='blue')
plt.xlabel('Years')
plt.ylabel('Average result')
plt.xticks(range(len(academic_years[int(choice) - 1])), academic_years[int(choice) - 1])
plt.yticks(range(0, 21, 2))
plt.show()
