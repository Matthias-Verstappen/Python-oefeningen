#oefening 8
wine = int(input("How many bottles of wine are there: "))
pizza = int(input("How many pizza's are there: "))

if wine >= 2 * pizza and wine >= 5 and pizza >= 5:
    print("This is a fantastic party!")
elif pizza >= 2 * wine and wine >= 5 and pizza >= 5:
    print("This is a fantastic party!")
elif wine >= 5 and pizza >= 5:
    print("This is a good party.")
elif wine < 5 or pizza < 5:
    print("This is just a stupid party.")
