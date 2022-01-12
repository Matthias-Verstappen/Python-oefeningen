# oefening 3

import xml.etree.ElementTree as ET

xml = ET.parse('Files/jobs.xml')
root = xml.getroot()

counter = 0
for company in root.find('jobs'):
    name_company = company[0].text
    contact_person = company[1].find('email').text #or company[1][1]
    vacancies = company.find('vacancies')
    for vacancy in vacancies:
        position = vacancy[0]
        if position.get('group')=='IT':
            counter += 1
            print(str(counter)+'\t','position',position.text)
            print('\tcompany:',name_company)
            print('\tContact person:',contact_person)