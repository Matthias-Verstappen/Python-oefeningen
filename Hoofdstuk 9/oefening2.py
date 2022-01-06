# oefening 2

import xml.etree.ElementTree as ET

xml = ET.parse('Files/cinemas.xml')
root = xml.getroot()

print('Bioscopen in Antwerpen')
for bioscoop in root.findall('bioscoopoverzicht'):
    print(bioscoop[4].text)
    print(bioscoop[5].text, bioscoop[6].text)
    print(bioscoop[7].text, bioscoop[8].text, '\n')