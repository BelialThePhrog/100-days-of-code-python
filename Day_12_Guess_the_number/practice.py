
# Namespace and Scope

enemies = 3

def increase_enemies():
    enemies = 2
    print(enemies)

# Shows local scope (prints 2)
increase_enemies()

# Shows global scope (prints 3)
print(enemies)

#Prime Number Checker

def is_prime(num):
    dividers = 0
    for i in range(1, num + 1):
        if num % (i) == 0:
            dividers += 1
            
    if num == 1:
        return False
    elif dividers > 2:
        return False
    else:
        return True

print(f"Is 73 a prime number? {is_prime(73)}")
