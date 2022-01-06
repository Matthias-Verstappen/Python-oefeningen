# oefening 8

ordered_scores = []
total_scores = 0
count = 0

print("Enter the scores for the test. Enter -1 if you want to finish.")
score = float(input("score: "))
while score != -1:
        total_scores += score
        ordered_scores.append(score)
        count += 1
        score = float(input("score: "))

print(f"The scores (ordered): {sorted(ordered_scores)} \nThe average of these {count} scores = {round(total_scores / count, 2)}")
