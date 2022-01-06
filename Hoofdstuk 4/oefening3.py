# oefening 3
import math

word = str(input("Enter a word with an odd number of letters: "))
number = math.floor(len(word) / 2 - 1)
third_number = number + 3

print(word[number: third_number])

#of zo
#
# text = input("Enter a word: ")
# middle= len(text)//2
# print(text[middle - 1:middle + 2])
