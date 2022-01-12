# oefening 3.1

import xml.etree.ElementTree as ET

xml = ET.parse('Files/jobs.xml')
root = xml.getroot()
count = 1

print('Overview IT vacancies:')

for company in root.iter('company'):
    company_name = company[0].text
    email = company[1][1].text
    vacancies = company.find('vacancies')
    for vacancy in vacancies:
        if vacancy[0].get('group')=='IT':
            print(f'{count}.\tPosition:\t{vacancy[0].text}')
            print(f'  \tCompany:\t{company_name}')
            print(f'  \tContact:\t{email}\n')
            count += 1
