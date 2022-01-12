# oefening 2.1

import xml.etree.ElementTree as ET

xml = ET.parse('Files/cinemas.xml')
root = xml.getroot()

print('Bioscopen in Antwerpen')
for cinema in root.findall('bioscoopoverzicht'):
    print(cinema[4].text)
    print(cinema[5].text, cinema[6].text)
    print(cinema[7].text, cinema[8].text, '\n')
