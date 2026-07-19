
# CAPSTONE: Guess the Number Game
import random as r

lives = 10

def initiation(max_num):
    random_number = r.randint(1, max_num)
    return random_number

print("Welcome to the Guessing Game")
choice = input("Please select the difficulty: 1, 2 or 3. ")

if choice == "1":
    max_num = 100
elif choice == "2":
     max_num = 250
elif choice == "3":
    max_num = 500
else:
    print("Invalid input, defaulting to difficulty 1.")
    max_num = 100 # Fallback in case of incorrect input

random_choice = initiation(max_num)

while lives > 0:
    print(f"The number is between 1 and {max_num}")
    Guess = int(input("What's your guess? "))
    
    if Guess == random_choice:
        print("Wow, you won!")
        break
    elif Guess > random_choice:
        lives -= 1
        print(f"Not this time. Guess lower. You have {lives} left")
    elif Guess < random_choice:
        lives -= 1
        print(f"Not this time. Guess higher. You have {lives} left")
else:
    print(f"Welp, you lost, the number was {random_choice}")
