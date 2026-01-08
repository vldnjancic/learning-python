student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

heights = 0
nr_students = 0

for i in student_heights:
    heights += i

for n in range(len(student_heights)):
    nr_students += 1

avg_height = round(heights / nr_students)

print(avg_height)
