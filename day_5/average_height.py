student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
num_students = 0

for height in student_heights:
    total_height += height
    num_students += 1
    avg_height = round(total_height / num_students)

# print(total_height)
# print(num_students)
print(f"The average height is {avg_height}.")