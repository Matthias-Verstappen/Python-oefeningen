# oefening 4

import matplotlib.pyplot as plt

labels = 'Football', 'Cricket', 'Formula1', 'Hockey'
sizes = [30.0, 15.0, 10.0, 45.0]
# colors =

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', counterclock=False, startangle=160)
ax1.axis('equal')

plt.title('Sports')
plt.show()

# from matplotlib import pyplot as plt
#
# labels = ["Cricket", "Football", "Hockey", "Formula 1"]
# percentages = [15, 30, 45, 10]
#
# plt.figure(figsize=(10, 10))  # --> DONUT GRAPH
# plt.pie(percentages, labels=labels, autopct='%1.2f%%') # percentages
# plt.show()