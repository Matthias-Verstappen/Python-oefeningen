# voorbeeld

print('Ex 1 Cities in USA')  # program start instructions
with open('Files/US cities.csv') as file:
    #   Denver;Colorado;727211
    line = file.readline().rstrip()
    record = line.split(';')

    while line:  # while not end of data
        state_indicative = record[1]  # group start instructions -> state = criteria
        print(state_indicative)
        max_population = int(record[2])
        max_city = record[0]
        # city_counter = 0

        while line and state_indicative == record[1]:  # while not end of data and same group
            print(f'\t{record[0]} - {record[2]}')
            if int(record[2]) > max_population:
                max_population = int(record[2])
                max_city = record[0]
            # city_counter += 1
            # print(f'\t{city_counter} {record[0]}')  # actions for each element of the group -> city
            line = file.readline().rstrip()  # take the next element of the group
            record = line.split(';')
        print(f'The largest population in {state_indicative} -> {max_city} - {max_population}')
    # group final instructions
    # program final instructions
