# Day 3 Learning - Control Flow and Logical Operators

# 1. Rollercoaster basic (if/else)
print("Welcome to the rollercoaster")
height = float(input("What's your height? "))
if height < 120:
    print("Can't ride it babe")
else:
    print("Have a nice ride!")

print("-" * 20)

# 2. Check if even or odd (Modulo operator)
print("Check if even!")
number = int(input("What's your number? "))
if number % 2 == 0:
    print("even")
else:
    print("odd")

print("-" * 20)

# 3. Rollercoaster with nested if/else and elif
payment = 0
print("Welcome to the rollercoaster")
height = float(input("What's your height? "))

if height < 120:
    print("Can't ride it babe")
else:
    age = int(input("What's your age? "))
    if age > 18:
        payment += 12
    elif age > 12:
        payment += 7
    else:
        payment += 5
        
    photo_QM = input("Do you want a photo? (Yes/No) ")
    if photo_QM == "Yes":
        payment += 3
        
    print(f"Your total is ${payment}")

print("-" * 20)

# 4. Pizza Delivery App
bill = 0
print("Welcome to the Python Pizza Delivery")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Extra Pepperoni? Y or N? ")
cheese = input("Extra Cheese? Y or N? ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Select correct option")

if pepperoni == "Y" and (size == "M" or size == "L"):
    bill += 5
elif pepperoni == "Y" and size == "S":
    bill += 3

if cheese == "Y":
    bill += 7

print(f"Your total is ${bill}")
