# Day 5 Project - Password Generator
import random as r

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']

print("Welcome to the PyPassword Generator!")
user_letter = int(input("How many letters would you like to have?\n"))
user_numbers = int(input("How many numbers would you like to have?\n"))
user_symbols = int(input("How many symbols would you like to have?\n"))

password_list = []

# Generate random characters based on user input
for _ in range(user_letter):
    password_list.append(r.choice(letters))

for _ in range(user_numbers):
    password_list.append(r.choice(numbers))

for _ in range(user_symbols):
    password_list.append(r.choice(symbols))

# Shuffle the final list to ensure true randomness
r.shuffle(password_list)

# Join the list back into a single string
new_final_password = "".join(password_list)

print(f"\nYour new password is: {new_final_password}")
