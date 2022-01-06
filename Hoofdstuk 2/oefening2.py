#oefening 2
birth_year = int(input('Enter your year of birth: '))
age = 2021 - birth_year
if age >= 18:
    print("Your age:", age, "\nSo, you're an adult.")
else:
    print("Your age:", age, "\nYou're not an adult yet.")