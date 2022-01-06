# oefening 4


total_number_certificates = 0
with open('Files/sponsors.txt') as file:
    list_sponsors = file.readlines()
    list_sponsors.sort()
    # print(*list_sponsors)
    print('Overview gifts')
    print('Number\tSponsor')
    # nr van sponsor in indicatief
    i = 0
    record = list_sponsors[i].rstrip().split('*')  # 1270*Wout*Beerens*10
    while i < len(list_sponsors):
        sponsor_indicative = record[0]
        total_per_sponsor = 0
        text_certificate = ''  # om sterretjes te regelen
        print(sponsor_indicative + '\t' + record[1] + '\t' + record[2], end='')
        while i < len(list_sponsors) and sponsor_indicative == record[0]:
            total_per_sponsor += int(record[3])  # convert om te kunnen tellen bedrag van de sponsoring
            i += 1
            if i < len(list_sponsors): # anders index out of range
                record = list_sponsors[i].rstrip().split('*')
        if total_per_sponsor > 40:
            total_number_certificates += 1
            text_certificate = '**'
        print('\t', total_per_sponsor, '\t', text_certificate)
    print(f'There are {total_number_certificates} tax certificates to be sent.')