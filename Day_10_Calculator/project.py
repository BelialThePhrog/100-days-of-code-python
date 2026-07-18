# Python Terminal Calculator
Continue = True

def addition(first_number, second_number):
    """Addition operation on R"""
    result = first_number + second_number
    print(f"Your outcome is: {result}")
    return result


def subtraction(first_number, second_number):
    """Subtraction operation on R"""
    result = first_number - second_number
    print(f"Your outcome is: {result}")
    return result


def multiplication(first_number, second_number):
    """Multiplication operation on R"""
    result = first_number * second_number
    print(f"Your outcome is: {result}")
    return result


def division(first_number, second_number):
    """Division operation on R"""
    result = first_number / second_number
    print(f"Your outcome is: {result}")
    return result

def wrong():
    """Incorrect Operator"""
    return "Wrong Operator"

print("Welcome to the Python Calculator")
first_number = float(input("Type in your first number: "))
operator = input("Choose the operation (+, -, *, /): ")

while Continue == True:
    second_number = float(input("Type in your second number: "))
    
    if operator == "+":
        first_number = addition(first_number, second_number)
    elif operator == "-":
        first_number = subtraction(first_number, second_number)
    elif operator == "*":
        first_number = multiplication(first_number, second_number)
    elif operator == "/":
        first_number = division(first_number, second_number)
    else:
        wrong()
        
    choice = input("Would you like to continue calculating? Y/N: ")
    if choice == "N" or choice == "n":
        Continue = False
        break
        
    operator = input("Choose the operation (+, -, *, /): ")
