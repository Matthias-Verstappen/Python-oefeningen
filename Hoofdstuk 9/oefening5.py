# oefening 5

import xml.etree.ElementTree as ET
root = ET.Element('compilation')

with open('Files/songs.txt') as file:
    line = file.readline().rstrip()
    while line:
        record = line.split(';')
        track = ET.Element('track')
        artist = ET.Element('artist')
        song = ET.Element('song')
        artist.text = record[0]
        song.text = record[1]
        root.append(track)
        track.append(artist)
        track.append(song)
        line = file.readline().rstrip()

tree = ET.ElementTree(root)
tree.write('songs.xml', encoding='utf-8', xml_declaration=True)