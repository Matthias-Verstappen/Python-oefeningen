# oefening 4.1

import xml.etree.ElementTree as ET

xmlDoc = ET.parse('Files/games.xml')
root = xmlDoc.getroot()

xml_types = set()
txt_types = set()

for types in root.iter('type'):
    xml_types.add(types.text)

with open('Files/games.txt') as file:
    line = file.readline().rstrip()
    while line:
        record = line.split(',')
        txt_types.add(record[7].strip("'"))
        line = file.readline().rstrip()

print(f'In the txt-file: {len(txt_types)} types of games.')
print(f'In the xml-file: {len(xml_types)} types of games.\n')
print('The types that occur in both files:')
print(xml_types.intersection(txt_types))
print()
print(f'The types that only appear in the txt-file:')
print(txt_types.difference(xml_types))
print()
print(f'The types that only appear in the xml-file:')
print(xml_types.difference(txt_types))