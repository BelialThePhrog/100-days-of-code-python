# Day 9 Learning - Dictionaries and Nesting

# 1. Dictionary Basics
print("--- Dictionary Basics ---")
programming_dictionary = {
    "apple": "A round fruit that grows on trees.",
    "python": "A programming language and also a type of snake.",
    "ocean": "A vast body of salt water covering much of the Earth.",
    "Loop": "The action of doing something."
}

# Accessing and adding elements
print(f"Definition of python: {programming_dictionary['python']}")
programming_dictionary["New Word"] = "NEW DEFINITION"

# Iterating over a dictionary
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")


# 2. Student Scores Exercise
print("\n--- Student Scores ---")
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "Outstanding" 
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations" 
    elif score >= 71:
        student_grades[student] = "Acceptable" 
    else:
        student_grades[student] = "Fail"

print(student_grades)


# 3. Nesting Lists and Dictionaries
print("\n--- Nesting ---")
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}    
print(f"Third city visited in France: {travel_log['France'][2]}")

letters = ["a", "b", ["c", "d"]]
print(f"Accessing nested list element: {letters[2][0]}")
