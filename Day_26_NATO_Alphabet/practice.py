import random as r

# --- List Comprehensions ---
my_list = [1,2,3,4]
new_list = [n+1 for n in my_list]
print(new_list)

name = "Kacper"
name_list = [letter for letter in name]
print(name_list)

new_list_2 = [number * 2 for number in range(1,5)]
print(new_list_2)

new_list_3 = [number * 2 for number in range(1,5) if number * 2 > 5]
print(new_list_3)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(number) for number in list_of_strings]
result = [number for number in numbers if number % 2 == 0]
print(result)

# --- Dictionary Comprehensions ---
letter_score = {letter:r.randint(0,100) for letter in name_list}
print(letter_score)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
split_sentence = sentence.split()
result = {word:len(word) for word in split_sentence}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
print(weather_f)
