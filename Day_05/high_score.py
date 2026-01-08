scores = input("Enter the scores:\n").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])

highest_score = 0
for i in scores:
    if i > highest_score:
        highest_score = i

print(f"The highest score in the class is: {highest_score}")