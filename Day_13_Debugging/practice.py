# ==========================================
# TASK 1: Input Validation
# ==========================================
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number. Please provide a numerical answer.")
    age = int(input("How old are you? "))


# ==========================================
# TASK 2: Odd or Even
# ==========================================
# Original Buggy Code:
# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."

# Fixed Code:
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


# ==========================================
# TASK 3: Leap Year
# ==========================================
# Original Buggy Code:
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# Fixed Code:
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# ==========================================
# TASK 4: FizzBuzz
# ==========================================
# Original Buggy Code:
# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# Fixed Code:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
