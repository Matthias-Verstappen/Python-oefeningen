# oefening 6

with open('Files/animal_sounds.txt') as file:
    animals = {}  # lege dictionary
    line = file.readline().rstrip()
    while line:
        record = line.split(';')
        animals[record[0]] = record[1]  # creëer key/value pair
        line = file.readline().rstrip()

# print(animals)

correct_answers = 0
print('Do you know the animal sounds?')
for key in animals:
    answer = input('What is the sound of ' + key + ': ')
    if answer == animals[key]:  # key is dier - value is geluid
        correct_answers += 1

print(correct_answers, 'correct answers')
