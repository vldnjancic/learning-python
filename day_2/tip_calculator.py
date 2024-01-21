print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill = total_bill / number_of_people
percentage = percentage_tip / 100
per_person = round(bill + bill * percentage, 2)
print(f"Each person should pay: ${per_person}")