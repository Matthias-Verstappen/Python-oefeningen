def lowest_price():
    prices = {}
    with open('Files/prices.txt') as file:
        line = file.readline().rstrip()
        record = line.split(';')
        while line:
            indicative_product = record[0]
            smallest_price = record[1]
            while line and record[0] == indicative_product:
                if float(record[1]) < float(smallest_price):
                    smallest_price = record[1]
                line = file.readline().rstrip()
                record = line.split(';')
            prices[indicative_product] = smallest_price
    return prices


prices_dict = lowest_price()
print('Print list:')
for item in prices_dict:
    print(item, '\t', prices_dict[item])

answer = input('Enter the item press x to stop\n')
while answer.upper().strip() != "X":
    if answer not in prices_dict:
        print("not available")
    else:
        print('Lowest price:', answer.lower(), 'is', prices_dict[answer])
    answer = input('Enter the item press x to stop\n')
