#extra oefening 1

limit = int(input("Geef een limiet in: "))

two_ago = 0
one_ago = 1

if limit == 0:
    print(0)
else:
    print(two_ago, end=", ")
    print(one_ago, end=", ")
    while two_ago + one_ago < limit:
        current = two_ago + one_ago
        two_ago = one_ago
        one_ago = current
        if one_ago + two_ago > limit:
            print(current, end="")
        else:
            print(current, end=", ")