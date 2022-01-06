# oefening 10
count = 0
for i in range(1, 4 + 1):
    count += 1
    name = str(input("Name: "))
    age = int(input("Age: "))
    member_years = int(input("Member for how many years: "))
    member_fee = 0
    if age < 12:
        member_fee = 20
    elif 12 <= age < 18:
        member_fee = 50
    elif age > 18:
        member_fee = 95

    if member_years >= 5:
        member_fee = member_fee * 0.9

print(f"Information for member {count}", "\nName:", name,
      "\nAge:", age, "\nMember for how many years:", member_years,
      f"\nMember fee for {name} = {member_fee}\n")

#Niet helemaal af