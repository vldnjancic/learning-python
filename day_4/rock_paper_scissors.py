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
the_game = [rock, paper, scissors]

user = int(input("What do you chose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
user_choice = the_game[user]
print(user_choice)
computer = random.randint(0, len(the_game) - 1)
computer_choice = the_game[computer]
print("Computer chose:")
print(computer_choice)

if user > computer:
    print("You Win.")
elif user == 0 and computer == 2:
    print("You Win.")
elif user == computer:
    print("It's a tie.")
else:
    print("You Lose.")