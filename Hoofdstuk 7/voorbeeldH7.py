# voorbeeld

# file = open('Files/students.txt') # opent connectie
#
# print(file.read()) # leest het volledige bestand
# file.close() # sluit connectie
#
#
# # alternatieve methode
#
# with open('Files/students.txt') as file: # opent en sluit automatisch
#     print(file.read()) # leest het volledige bestand
#

# lezen lijn per lijn

# with open('Files/students.txt') as file:
#     line = file.readline()  # stap 1 in inlezen
#     while line:  # step 2 while -> checkt de voorwaarde -> zolang er lijnen zijn
#         if line != '\n':  # stap 3 -> verwerken
#             print(line.rstrip('\n'))
#             # alternatief -> print(line, end='')
#         line = file.readline()  # stap 4 -> opnieuw lezen


# Lezen zonder jaartal

# with open('Files/students.txt') as file:
#     line = file.readline()  # stap 1 in inlezen
#     while line:  # step 2 while -> checkt de voorwaarde -> zolang er lijnen zijn
#         if line != '\n':  # stap 3 -> verwerken
#             # Brent;Aerts;2002\n
#             record = line.split(";") # lijst gemaakt door te splitsen bij de ";" -> uit voorbeeld -> Brent = 0, Aerts = 1, 2002\n -> 2
#             print(record[0], record[1])
#         line = file.readline()  # stap 4 -> opnieuw lezen


# lezen in een lijst

with open('Files/students.txt') as file:
    lines = file.readlines() # alleen gebruiken als je lijst nodig heeft, gebruikt veel meer resources dan readline()
print(lines)