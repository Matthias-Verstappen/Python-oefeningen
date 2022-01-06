# oefening 4
import xml.etree.ElementTree as ET

# 'Schattenjacht','Haba',null,2003,'vanaf 5j',2,6,'educational','15 min',null,17.50,'schattenjacht.jpg'
# inlezen txt
with open('Files/games.txt', encoding='utf-8') as file:
    types_txtfile = set()  # lege set voor types van txt file
    line = file.readline().rstrip()
    while line:
        record = line.split(',')
        type_game = record[7].strip("'").strip('').lower()
        # weg single quote, weg spaties, alles kleine letters
        types_txtfile.add(type_game)
        line = file.readline().rstrip()

# print(types_txtfile)

# inlezen xml
xmlDoc = ET.parse('Files/games.xml')
root = xmlDoc.getroot()
types_xmlfile = set()  # lege set voor types van xml file

for game in root.iter('game'):  # findall -> direct children of root
    types_xmlfile.add(game[1].text.lower())
# print(types_xmlfile)
print('In the txt file', len(types_txtfile), 'types of games')
print('In the xml file', len(types_xmlfile), 'types of games')

print('Types in both files:')
print(types_txtfile.intersection(types_xmlfile))  # gemeenschappelijke types
print('Types only in txt file:')
print(types_txtfile.difference(types_xmlfile))
print('Types only in xml file:')
print(types_xmlfile.difference(types_txtfile))
# difference delivers a set that only occurs in the first set and not in the second set.
