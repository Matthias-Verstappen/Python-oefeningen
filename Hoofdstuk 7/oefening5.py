#oefening 5

with open('Files/books.txt') as books:
    line = books.readline().rstrip() # lezen eerste boek
    count = 1 # hulpvar voor opsomming
    while line:
        author = books.readline().rstrip() # lezen auteur
        count += 1
        print(str(count) + '. ' + line.rstrip() + ' -> ' + author.rstrip())
        line = books.readline() #opnieuw lezen