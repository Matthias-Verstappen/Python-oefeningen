# herhalingsoefening 4

# milk;1.07;Colruyt

def lowest_price():
    prices = {}  # dictionary
    with open('Files/prices.txt') as file:
        line = file.readline().rstrip()
        record = line.split(';')
        while line:
            product_indicative = record[0]  # grouping per product
            smallest_price = record[1]
            while line and record[0] == product_indicative:  # per product
                if float(record[1]) < float(smallest_price):  # kleinste prijs zoeken per product
                    smallest_price = record[1]
                line = file.readline().rstrip()
                record = line.split(';')
            prices[product_indicative] = smallest_price  # create key/value pair
    return prices


# hoofdprogramma
# print(lowest_price())
prices_dict = lowest_price()
# print('Print list:')
# for item in prices_dict:  # item is de key
#     print(item, '\t', prices_dict[item])  # key value(naam van dict[key])

answer = input('Enter the item, press X to stop: ')
while answer.upper() !='X':
    if answer not in prices_dict:
        print('Not available')
    else:
        print('Lowest price for', answer.lower(), 'is', prices_dict[answer])
    answer = input('Enter the item, press X to stop: ')
