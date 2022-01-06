#oefening 12
age = int(input("Your age = "))

if age < 6:
    print("You're too young!")
elif age == 6 or age == 7:
    print("You'll be assigned to the Beavers.")
elif 8 <= age <= 10:
    print("You'll be assigned to the Cubs.")
elif 11 <= age <= 13:
    print("You'll be assigned to the Scouts.")
elif 14 <= age <= 18:
    print("You'll be assigned to the Explorers.")
else:
    print("You'll be assigned to the Leaders.")