import random

name_string = input("Give me everybody's names, separated by a comma: ")
names = name_string.split(", ")

choice = random.randint(0, len(names) - 1)
person_to_pay = names[choice]
print(f"{person_to_pay} is going to pay the bill.")