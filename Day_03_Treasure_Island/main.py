# Day 3 Project - Treasure Island

print("Welcome to Treasure Island!")
print("Your mission is to find the hidden treasure.")

choice_1 = input('You\'re at a crossroad. Where do you want to go? Type "Left" or "Right"\n').capitalize()

if choice_1 == "Right":
    print("You fell into a hole. Game Over.")
else:
    choice_2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a boat. Type "Swim" to swim across.\n').capitalize()
    if choice_2 == "Swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        choice_3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? (Red, Yellow, Blue)\n').capitalize()
        if choice_3 == "Yellow":
            print("You found the treasure! You Win!")
        elif choice_3 == "Red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "Blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
