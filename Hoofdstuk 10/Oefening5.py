# oefening 5

months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
          "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

choice = input('Month (press enter if you want to see an overview) ').capitalize()
if choice == '':  # single single -> lege string
    for key in months:
        print(key, '\t', months[key])  # print key tab value
else:
    print(months.get(choice.capitalize(), 'This month does not exist.'))  # value geven of boodschap tonen
