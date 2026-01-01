print("Welcome to the love calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

true = str(t + r + u + e)
love = str(l + o + v + e)
compatibility = int(true + love)

if compatibility < 10 | compatibility > 90:
    print(f"Your score is {compatibility}%, you go together like coke and menthos.")
elif compatibility >= 40 | compatibility <= 50:
    print(f"Your score is {compatibility}%, you are alright together.")
else:
    print(f"Your score is {compatibility}%.")
