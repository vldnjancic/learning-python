print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")
crossroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if crossroad == "left":
    print("You fell into a hole with spikes. Game Over!")
    exit
else:
    lake = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if lake == "swim":
        print("You were eaten by crocodiles. Game Over!")
        exit
    else:
        island = input('You arrive at the island unharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
        if island == "red":
            print("You entered a room with fire. Game Over!")
            exit
        elif island == "yellow":
            print("You went into a room with snakes. Game Over!")
            exit
        elif island == "blue":
            print("You found the treasure! You Win!")