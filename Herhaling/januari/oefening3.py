# oefening 3

# imports
import random
import xml.etree.ElementTree as ET


# functies
# Carl/Kurt/Niels/Klaus/Rik -> indexen van 0 tem 4

def read_names():
    names = []
    with open('Files/names.txt') as file:
        line = file.readline().rstrip()
        while line:
            record = line.split('/')
            random_number = random.randint(0, 4)  # len(record)-1
            names.append(record[random_number])
            line = file.readline().rstrip()
    names.sort()
    return names


def read_figures():
    figures = []  # lege lijst
    xmlDoc = ET.parse('Files/figures.xml')
    root = xmlDoc.getroot()
    for figure in root.iter('figure'):  # findall()
        figures.append(figure[1].text + ' ' + figure[0].text) # neem kleur en vorm
    return figures

# print(read_figures())
figures_list = read_figures()
names_list = read_names()
print('A figure has been chosen for the following toddlers:')
for name in names_list:
    length = len(name)
    figure = figures_list[length-1] # Arne -> 4 letters -> 3de element uit de lijst halen
    print(name, '\t', figure)