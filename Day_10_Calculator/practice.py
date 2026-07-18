
#  Basic Functions with Return Values

def my_function():
    result = 3 * 2
    return result 

print(my_function())

# Formatting & Live Input Validation

name = input("What's your name? ")
surname = input("What's your surname? ")

def format_name(name, surname):
    if name == "" or surname == "":
        return "You did not provide valid letters"
    new_name = name.title()
    new_surname = surname.title()
    result = (f"Your new name: {new_name} {new_surname}")
    return result

print(format_name(name, surname))

# Leap Year Conditional Logic

def is_leap_year(year):
    """Checking if the year is a leap year"""
    if year % 4 == 0:
        if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
            return True
        else: 
            return False
    else:
        return False
        
print(f"Is 2400 a leap year? {is_leap_year(2400)}")
print(f"Is 1989 a leap year? {is_leap_year(1989)}")
