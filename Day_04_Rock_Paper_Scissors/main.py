# Day 4 Project - Rock, Paper, Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors Game!")
user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n")) - 1

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"\nYou chose:\n{game_images[user_choice]}")
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{game_images[computer_choice]}")
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw!")
