#oefening 2.2

birth = int(input('Enter your year of birth: '))
age = 2021 - birth

print(f'Your age = {age}')
if age >= 18:
    print("So you're an adult.")
else:
    print("You're not an adult yet.")