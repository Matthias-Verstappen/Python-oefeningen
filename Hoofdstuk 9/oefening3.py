# oefening 3

import xml.etree.ElementTree as ET

xml = ET.parse('Files/jobs.xml')
root = xml.getroot()

print('Overview IT vacancies:')
count = 1
for jobs in root.iter('company'):
    print(count, '.\tPosition:\t', end='')
    for vacancy in jobs.iter('vacancies'):
        print(vacancy[0].text)