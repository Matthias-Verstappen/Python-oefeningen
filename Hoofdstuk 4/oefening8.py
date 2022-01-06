#oefening 8

word = str(input("Enter a word: "))

# if word[:2] == "in" or word[1:3] == "in":
#     print(f"'in' appears in the first or second place.")
# elif "in" in word[3:]:
#     print("'in' appears in the word, but not in front.")
# else:
#     print("this word does not contain 'in'")

if word.find("in") == (0,1):
    print(f"'in' appears in the first or second place.")
elif word.find("in") > 1:
    print("'in' appears in the word, but not in front.")
else:
    print("this word does not contain 'in'")
