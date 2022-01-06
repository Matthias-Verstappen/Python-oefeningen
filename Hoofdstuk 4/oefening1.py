#oefening 1

kleur = str(input("What's your favourite colour: "))

print(kleur[0:3:2]) #of print(kleur[0] + kleur[2])
print(f"This colour consists of {len(kleur)} letters.\n")

for letter in kleur:
    print(f"{letter} = {ord(letter)}")


i = 0
while i < len(kleur):
    if i % 2 == 0:
        print(f"#{kleur[i]}#")
        i += 1
    else:
        print(f"**{kleur[i]}**")
        i += 1