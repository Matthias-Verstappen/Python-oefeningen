# oefening 5.1

with open('Files/books.txt') as file:
    title = file.readline().rstrip()
    count = 0
    while title:
        author = file.readline().rstrip()
        count += 1
        print(f'{count}.\t{title} -> {author}')
        title = file.readline().rstrip()
