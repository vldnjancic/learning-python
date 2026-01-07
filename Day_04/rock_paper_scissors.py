import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
choice = [rock, paper, scissors]

rand_choice = random.randint(0, len(choice) - 1)
user_choice = choice[user]
computer_choice = choice[rand_choice]
print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user == 0 and rand_choice == 2:
    print("You Win!")
elif user == 2 and rand_choice == 0:
    print("You Lose.")
elif rand_choice > user:
    print("You Lose.")
elif user == rand_choice:
    print("It's a tie.")
else:
    print("You Win!")
