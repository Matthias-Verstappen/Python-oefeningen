#oefening 3.1
import math

word = input('Enter a word: ')

length = len(word)
half_length = length // 2

print(word[half_length-1:half_length+2])