#oefening 1

import xml.etree.ElementTree as ET

xml = ET.parse('Files/plants.xml')
root = xml.getroot()
count = 1

for plant in root.iter('plant'):
    if plant[3].text == 'SUN':
        print('Plant', count,':', plant[0].text, '(' + plant[1].text.capitalize() + ')')
        count += 1
