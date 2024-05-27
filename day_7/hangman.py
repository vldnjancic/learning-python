import random
from hangman_art import stages, clear_screen, logo
from hangman_words import word_list

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

hidden_word = []
for i in chosen_word:
    hidden_word += "_"

print(logo)
end_of_game = False
lives = 6

while end_of_game != True:
    guess = input("Guess a letter: ").lower()

    clear_screen()

    if guess in hidden_word:
        print(f"You've already entered {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            hidden_word[position] = guess

    if guess not in chosen_word:
        print(f"You've guessed {guess}, it's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The answer was {chosen_word}")

    print(f"{''.join(hidden_word)}")

    if "_" not in hidden_word:
        end_of_game = True
        print("You Win!")

    print(stages[lives])


# if guess in chosen_word:
#     print("Correct")
