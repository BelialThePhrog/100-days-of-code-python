# Day 4 Learning - Randomization and Python Lists
import random

# 1. Random Module Basics
print("Random Integer (20-30):", random.randint(20, 30))
print("Random Float (10-20):", random.uniform(10, 20))

print("-" * 20)

# 2. Heads or Tails
print("Heads or Tails Game")
outcome = random.randint(0, 1)
if outcome == 1:
    print("Heads")
else:
    print("Tails")

print("-" * 20)

# 3. Lists Basics
fruits = ["apples", "Peach", "Pear"]
print(f"First fruit: {fruits[0]}")

fruits.append("Grapes")
print(f"Last fruit after append: {fruits[-1]}")

fruits.extend(["Banana", "Kiwi"])
print(f"List after extend: {fruits}")

print("-" * 20)

# 4. Who will pay the bill?
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Method 1 (using randint)
random_index = random.randint(0, len(friends) - 1)
print(f"Method 1: Today {friends[random_index]} will pay.")

# Method 2 (using choice)
print(f"Method 2: Today {random.choice(friends)} will pay.")

print("-" * 20)

# 5. Nested Lists
fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

dirty_dozen = [fruits, vegetables]
print("Nested List (Dirty Dozen):")
print(dirty_dozen)
