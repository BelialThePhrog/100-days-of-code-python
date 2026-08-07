# Exception Catching Practice

try:
    # Attempting an operation that will trigger a TypeError
    result = 7 + "problem"
except:
    # Catching any exception and handling it without crashing
    print("Error")
