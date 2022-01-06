# oefening 4.1


# 1270*Wout*Beerens*10

# with open('Files/sponsors.txt') as file:
#     line = file.readline().rstrip()
#     record = line.split('*')
#     certificate_count = 0
#     while line:
#         sponsor_ind = record[0]
#         name = record[1] + ' ' + record[2]
#         total = int(record[3])
#         while line and sponsor_ind == record[0]:
#             total += int(record[3])
#             line = file.readline().rstrip()
#             record = line.split('*')
#         if total > 200:
#             certificate_count += 1
#         print(f'{sponsor_ind}\t{name}\t{total}')