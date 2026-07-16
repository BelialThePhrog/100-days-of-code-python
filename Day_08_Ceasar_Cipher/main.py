# Day 8 Project - Caesar Cipher

print("Welcome to the Caesar Cipher")

list_of_letters = list("abcdefghijklmnopqrstuvwxyz")

def encrypt(final_text, shift_amount):
    outcome = ""
    for letter in final_text:
        before_shift = list_of_letters.index(letter)
        # The alphabet has 26 letters, so we use modulo 26 to wrap around
        after_shift = (before_shift + shift_amount) % 26
        outcome += list_of_letters[after_shift]
    print(f"Your encrypted message: {outcome}")

def decrypt(final_text, shift_amount):
    outcome = ""
    for letter in final_text:
        before_shift = list_of_letters.index(letter)
        after_shift = (before_shift - shift_amount) % 26
        outcome += list_of_letters[after_shift]
    print(f"Your decrypted message: {outcome}")

choice = input("Would you like to 'encrypt' or 'decrypt'?\n").lower()

if choice in ["encrypt", "decrypt"]:
    message = input("Provide the Message (only letters and spaces):\n")
    shift = int(input("Please provide the Shift:\n"))
    
    # Text preparation
    final_message = message.replace(" ", "").lower()
    
    if choice == "encrypt":
        encrypt(final_message, shift)
    elif choice == "decrypt":
        decrypt(final_message, shift)
else:
    print("Invalid input! Please type 'encrypt' or 'decrypt'.")
