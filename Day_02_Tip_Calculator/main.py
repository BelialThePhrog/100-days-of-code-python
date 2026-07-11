# Day 2 Project - Tip Calculator

print("Welcome to the Tip Calculator!")
price = float(input("How much was the bill? "))
people = int(input("How many people were there? "))
tip = str(input("Do you want to leave a tip? Yes/No "))

if tip == "Yes":
    tip_per = float(input("How much tip? "))
else:
    tip_per = 0

total = round((price * (1 + tip_per/100) / people), 2)
print(f"Your total per person is {total}")
