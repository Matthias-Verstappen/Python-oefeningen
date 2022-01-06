# oefening 6


# deel 1 zonder for
# txt = input("Enter a text:  ").replace(" ","")
# lst = [*txt]
#
# print(lst)
# print(*lst,sep=" ")
# print(*lst,sep="   ")

# deel 1 met for
txt = input("Enter a text:  ").replace(" ","")
lst = []
for i in txt:
        lst.append(i)
lst = sorted(lst)
lst = [*txt]
print(lst)
print(*lst,sep=" ")
print(*lst,sep="   ")

# deel 2
txt = input("Enter a text:  ").replace(" ","")

for i in txt:
    if i not in lst:
        lst.append(i)
lst = sorted(lst)

print(lst)
print(*lst,sep=" ")
print(*lst,sep="   ")






































# def string_to_list(string):
#     list1 = []
#     list1[:0] = string.replace(" ", "")
#     return list1

# text = input("Enter a text: ").replace(" ", "")
# print(text)
# text_list = string_to_list(text)
# print(text_list, "\n")



# i = 0
# while i < len(text_list):
#     print(text_list[i], end=" ")
#     i += 1
#
# print("\n")
#
# j = 0
# while j < len(text_list):
#     print(text_list[j], end="   ")
#     j += 1