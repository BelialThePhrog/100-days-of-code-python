# Day 5 Learning - For Loops, Range, and Code Blocks

# 1. Basic For Loop
fruits = ["Apples", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

print("-" * 20)

# 2. Iterating with slices and accumulating a sum
scores = [
    80, 82, 84, 86, 88,
    90, 92, 94, 96, 98,
    100, 102, 104, 106, 108,
    110, 112, 114, 116, 120
]

total_sum = 0 
for student in scores[1:18:2]:
    total_sum += student
print(f"Sum of slice: {total_sum}")

print("-" * 20)

# 3. Finding max value using a loop manually
max_score = 0
for student in scores:
    if student > max_score:
        max_score = student
print(f"Max score is: {max_score}")

print("-" * 20)

# 4. Using range() function
sum_1 = 0
for number in range(0, 100, 5):
    sum_1 += number
print(f"Sum using range: {sum_1}")
