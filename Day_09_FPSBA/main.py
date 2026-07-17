# Day 9 Project - Secret Auction (FPSBDA)
import os

# Function to clear the console across different operating systems
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Secret Auction (First-Price Sealed-Bid Auction)!")

bidders = {}
bidding_finished = False

while not bidding_finished:
    name = input("What's your name? ")
    bid = int(input("How much do you bid? $"))
    
    # Store the bid in the dictionary
    bidders[name] = bid
    
    choice = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
    if choice == "no":
        bidding_finished = True
    else:
        # Clear the screen so the next person can't see the previous bid
        clear_console()

# Find the winner
# Using Python's built-in max function with a key argument to find the highest value
winner = max(bidders, key=bidders.get)
highest_bid = bidders[winner]

clear_console()
print("The auction is over!")
print(f"The winner is {winner} with a bid of ${highest_bid}!")
