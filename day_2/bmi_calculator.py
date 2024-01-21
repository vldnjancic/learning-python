height = float(input("Enter your height in m: "))
weight = int(input("Enter your wight in kg: "))

bmi = round(weight / height ** 2)
print(f"Your BMI is {bmi}")