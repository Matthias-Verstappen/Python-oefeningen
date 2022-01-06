#oefening 8.1
scores = []
count = 0
print('Enter the scores for the test. Use -1 if you want to finish.')
score = float(input('Score: '))

while score != -1:
    scores.append(score)
    count += 1
    score = float(input('Score: '))

ordered_scores = sorted(scores)
average = 0
for i in range(len(scores)):
    average += scores[i]
average = round((average / count), 2)

print(f'The scores (ordered): {ordered_scores}')
print(f'The average of these {count} scores = {average}')