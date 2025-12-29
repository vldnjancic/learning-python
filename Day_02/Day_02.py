print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
nr_people = int(input("How many people are splitting the bill? "))
split_bill = total_bill / nr_people
bill = round((split_bill) * (percentage_tip * 0.01) + split_bill, 2)
print(f"Each person should pay: ${bill}")