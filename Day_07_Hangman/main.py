# Day 7 Project - Hangman Game
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = [
    "apple", "river", "mountain", "chair", "window", "ocean", "forest", "pencil",
    "computer", "banana", "guitar", "camera", "planet", "garden", "butterfly",
    "library", "coffee", "blanket", "rocket", "diamond", "sunshine", "bridge",
    "castle", "dragon", "flower", "island", "lantern", "mirror", "notebook",
    "orange", "penguin", "quilt", "rainbow", "sandwich", "telescope", "umbrella",
    "volcano", "waterfall", "xylophone", "yogurt", "zebra", "anchor", "balloon",
    "candle", "desert", "eagle", "feather", "glacier", "harbor", "iceberg",
    "jungle", "kettle", "lighthouse", "meadow", "necklace", "orchard", "pyramid",
    "suitcase", "treasure", "violin"
]

word_to_guess = random.choice(word_list)
lives = 6
missed = 0
already_guessed = []

# Create the initial display (e.g., ['_', '_', '_'])
display = ["_"] * len(word_to_guess)

print("Welcome to HANGMAN!")
print(" ".join(display))

while lives > 0 and "_" in display:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in already_guessed:
        print(f"You've already guessed '{guess}'. Try again.")
        continue
        
    already_guessed.append(guess)
    
    if guess in word_to_guess:
        print("Nice! You got it.")
        for position, letter in enumerate(word_to_guess):
            if letter == guess:
                display[position] = guess
    else:
        print("Unlucky! That letter is not in the word.")
        lives -= 1
        missed += 1
        print(f"You have {lives} lives left.")
        
    print(f"Already guessed: {', '.join(already_guessed)}")
    print(" ".join(display))
    print(HANGMANPICS[missed])

if lives > 0:
    print("\nYou WON! Congratulations!")
else:
    print(f"\nYou lost! :< The word was: {word_to_guess}")
