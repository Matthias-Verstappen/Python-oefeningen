# oefening 9
import re

lunch = str(input("What do you eat for lunch: "))

if lunch.count("sandwich") < 2:
    print('')
else:
    slice_place1 = lunch.find("sandwich")
    lunch = lunch[slice_place1 + 8:]
    slice_place2 = lunch.find("sandwich")
    lunch = lunch[:slice_place2]
    print(f"You have {lunch} between your sandwich")