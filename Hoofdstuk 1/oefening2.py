#oefening 2

yes = int(input("How many people voted YES: "))
no = int(input("How many people voted NO: "))
blank = int(input("Number of blank votes: "))

percentage_yes = yes / (yes + no + blank) * 100
percentage_no = no / (yes + no + blank) * 100
percentage_blank = blank / (yes + no + blank) * 100

print(f'YES: {percentage_yes}%\n'
      f'NO: {percentage_no}%\n'
      f'Blank: {percentage_blank}%')