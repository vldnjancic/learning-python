from os import replace
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

print(chosen_word)

hidden_word = []
for i in chosen_word:
    hidden_word += "_"
print(hidden_word)


def position():
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            hidden_word[position] = guess

while "_" in hidden_word:
    guess = input("Guess a letter: ").lower()
    position()
    print(hidden_word)
    if "_" not in hidden_word:
        print("You Win!")
        exit()

# if guess in chosen_word:
#     print("Correct")
