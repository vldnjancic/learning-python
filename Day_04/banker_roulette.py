import random

names = input("Enter the names, separated by a comma:\n").split(", ")
random_number = random.randint(0, len(names))
person_to_pay = names[random_number]

print(f"{person_to_pay} is paying the bill.")
