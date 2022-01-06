#voorbeeld 1 van hoofdstuk 2
#checking a password
#step 1: declaration and input
password = input('Password? ')
age = int(input("Age? "))
#step 2: checking condition -> True or False
if password == 'Corona' and age >= 18:
    print('Access granted')
    print('Cheers')
else:
    print('Access denied')
