# lesvoorbeeld

import xml.etree.ElementTree as ET

xmlDoc = ET.parse("Files/drugs.xml")
root = xmlDoc.getroot()

# for item in root:
#     print(item.tag, item.attrib)
#
# print('root[1].tag + attribute:', root[1].tag, root[1].get('code'))
# print('root[0][3].tag: ', root[0][3].tag)
# print('root[0][3].text: ', root[0][3].text)

for leaflet in root.findall('leaflet'): # of iter (is sterker)
    # print(leaflet[0].text + ':' + leaflet[3].text)
    name = leaflet.find('name')
    group = leaflet.find('group')
    print(name.text, ':', group.text)
    print('\tPharmaceutical forms:')
    for form in leaflet[1]:
        print('\t\t', form.text)