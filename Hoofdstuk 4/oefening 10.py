# #oefening 10
#
# word1 = str(input("Enter word 1: "))
# word2 = str(input("Enter word 2: "))
# word3 = str(input("Enter word 3: "))
# word4 = str(input("Enter word 4: "))
# word5 = str(input("Enter word 5: "))
#
# sentence = f"{word5} {word4} {word3} {word2} {word1}"
#
# # print(f"The words in reverse order:\n ")
#
# print(sentence.lower().capitalize())

sentence = ""
for i in range(1,6):
    word = str(input("Enter word " + str(i) + ": ")).capitalize()
    sentence = word + ' ' + sentence

print("The words in reverse order: ")
print(sentence)