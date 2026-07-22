import coffee_maker
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
coffee_maker.report()


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? {options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in options:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"That will be{drink.cost}")
            money_machine.make_payment(drink.cost)
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)
