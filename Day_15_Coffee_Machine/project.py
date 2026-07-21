#Coffee Machine
coffees = [
    {
        "name": "Espresso",
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "money": 2.50
    },
    {
        "name": "Americano",
        "water": 150,
        "milk": 0,
        "coffee": 18,
        "money": 3.00
    },
    {
        "name": "Cappuccino",
        "water": 30,
        "milk": 120,
        "coffee": 18,
        "money": 3.80
    },
    {
        "name": "Latte",
        "water": 30,
        "milk": 180,
        "coffee": 18,
        "money": 4.20
    },
    {
        "name": "Flat White",
        "water": 30,
        "milk": 150,
        "coffee": 18,
        "money": 4.00
    }
]

coffees_list = ["espresso","americano", "cappuccino", "latte",  "flat white"]
#starting resources
water = 3000
milk = 2000
coffee = 200 
coins = [0.25, 0.10, 0.05, 0.01]
quaters = 100
dimes = 100
nickles = 100
pennies = 100
money = pennies *0.01 + nickles*0.05 + dimes*0.10 + quaters*0.25

def report_print():
    """Report printing"""
    print(f"Water: {water}ml \n Milk: {milk}ml \n Coffee: {coffee}g \n Money: {money}$")

def is_sufficient():
    """checking if enough resources"""
    if (water < coffees[coffee_index]["water"] or
        milk < coffees[coffee_index]["milk"] or
        coffee < coffees[coffee_index]["coffee"]):
        print("Not enough resources to make that coffee.")
        return False
    else:
        print(f"We can do that. Please provide: {coffees[coffee_index]['money']}$")
        return True

def payment(quaters, dimes, nickles, pennies):
    """Paying for coffee"""
    quaters_curr = int(input("How many quaters?"))
    dimes_curr = int(input("How many dimes?"))
    nickles_curr = int(input("How many nickles?"))
    pennies_curr = int(input("How many pennies?"))
    payment = quaters_curr * 0.25 + dimes_curr * 0.1 + nickles_curr * 0.05 + pennies_curr * 0.01

    if payment < coffees[coffee_index]["money"]:
        money_missing = round(coffees[coffee_index]["money"] - payment,2)
        print(f"Not enough. You are missing:{money_missing}")
    else:
        change = payment - coffees[coffee_index]["money"]
        
    
        while round(change, 2) > 0: 
            quaters_to_give = min(int(round(change // 0.25)), quaters)
            if quaters_to_give < quaters:
                quaters -= quaters_to_give
                change -= quaters_to_give*0.25
            else:
                quaters_to_give = quaters
                quaters -= quaters
                change -= quaters_to_give*0.25
            
            dimes_to_give = min(int(round(change // 0.10)), dimes)
            if dimes_to_give < dimes:
                dimes -= dimes_to_give
                change -= dimes_to_give*0.10
            else:
                dimes_to_give = dimes
                dimes -= dimes
                change -= dimes_to_give*0.10
            
            nickles_to_give = min(int(round(change // 0.05)), nickles)
            if nickles_to_give < nickles:
                nickles -= nickles_to_give
                change -= nickles_to_give*0.05
            else:
                nickles_to_give = nickles
                nickles -= nickles
                change -= nickles_to_give*0.05
            
            pennies_to_give = min(int(round(change // 0.01)), pennies)
            if pennies_to_give < pennies:
                pennies -= pennies_to_give
                change -= pennies_to_give*0.01
            else:
                pennies_to_give = pennies
                pennies -= pennies
                change -= pennies_to_give *0.01
            total = pennies_to_give *0.01 + nickles_to_give*0.05 + dimes_to_give*0.10 + quaters_to_give*0.25
            if round(change, 2) == 0:
                print(f"Here is your change: {quaters_to_give} quaters {dimes_to_give} dimes {nickles_to_give} nickles {pennies_to_give} pennies. Total: {total}")
                quaters += quaters_curr
                dimes += dimes_curr 
                nickles += nickles_curr
                pennies +=  pennies_curr
                break
            else:
                print("Sorry, we can't provide change.")
                break
        else:
            print("Thank You!")
    return quaters, dimes, nickles, pennies

def making_coffee(water, milk, coffee):
    """Making coffee"""
    global money
    water -= coffees[coffee_index]["water"]
    milk -= coffees[coffee_index]["milk"]
    coffee -= coffees[coffee_index]["coffee"]
    money += coffees[coffee_index]["money"]
    return water, milk, coffee
    
#Main Body
is_another_one = True
while is_another_one == True:
    try:
        choice = input("What would you like? (espresso/latte/cappuccino/flat white/americano):").lower()
        if choice not in ["espresso", "latte", "cappuccino", "flat white", "americano" , "report", "off"]:
                raise ValueError("Invalid choice.")
    except ValueError:
        print("You have typed in invalid coffee. Please provide choice from the list")
        choice = input("What would you like? (espresso/latte/cappuccino/flat white/americano):").lower()
        
    if choice == "report":
        report_print()
    elif choice == "off":
        print("Shutting down") 
    elif choice in ["espresso","americano", "cappuccino", "latte",  "flat white"]:
        coffee_index = coffees_list.index(choice)
        is_sufficient_value = is_sufficient()
        while is_sufficient_value == True:
            quaters, dimes, nickles, pennies = payment(quaters, dimes, nickles, pennies)
            water, milk, coffee = making_coffee(water, milk, coffee)
            print(f"Enjoy your {choice}!")
            another_one = input("Would you like another one? Y/N").upper()
            if another_one == "N":
                is_another_one = False
            break
        else:
            print("Sorry, we can't do that")
