# Matthias Verstappen
# r0851784
# 1 ITF 11

name = input('Please enter your first- and last name: ')
welcome = f"Welcome {name}"
print(welcome)
print("_" * len(welcome))

for i in range(len(name) + 1):
    print(name[:i])