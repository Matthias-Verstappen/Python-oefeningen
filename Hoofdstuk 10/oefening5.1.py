# oefening 5.1

months = {"January" : 31,
"February" : 28,
"March" : 31,
"April" : 30,
"Mai" : 31,
"April" : 30,
"May" : 31,
"June" : 30,
"July" : 31,
"August" : 31,
"September" : 30,
"October" : 31,
"November" : 30,
"December" : 31}


entry = input('Month (press enter in you want to see an overview of all months): ')

if entry == "":
    for month in months:
        print(month, months[month])
else:
    print(months.get(entry.capitalize(), "This month does not exist"))