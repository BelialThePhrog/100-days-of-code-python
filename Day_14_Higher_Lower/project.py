#Final Project for Begginer Section
import random as r
from IPython.display import clear_output
import time as t
data = [
    {"name": "Cristiano Ronaldo", "follower_count": 660, "description": "footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 510, "description": "footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 420, "description": "singer and actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 400, "description": "media personality", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 395, "description": "actor and wrestler", "country": "United States"},
    {"name": "Ariana Grande", "follower_count": 375, "description": "singer", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 360, "description": "media personality", "country": "United States"},
    {"name": "Beyoncé", "follower_count": 315, "description": "singer", "country": "United States"},
    {"name": "Khloé Kardashian", "follower_count": 305, "description": "television personality", "country": "United States"},
    {"name": "Nike", "follower_count": 305, "description": "sportswear brand", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": 295, "description": "singer", "country": "Canada"},
    {"name": "Kendall Jenner", "follower_count": 285, "description": "model", "country": "United States"},
    {"name": "Taylor Swift", "follower_count": 280, "description": "singer-songwriter", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": 275, "description": "cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "follower_count": 250, "description": "singer and actress", "country": "United States"},
    {"name": "National Geographic", "follower_count": 285, "description": "magazine", "country": "United States"},
    {"name": "Neymar Jr.", "follower_count": 230, "description": "footballer", "country": "Brazil"},
    {"name": "Nicki Minaj", "follower_count": 225, "description": "rapper", "country": "United States"},
    {"name": "Kourtney Kardashian", "follower_count": 220, "description": "television personality", "country": "United States"},
    {"name": "Miley Cyrus", "follower_count": 210, "description": "singer", "country": "United States"},
    {"name": "Katy Perry", "follower_count": 205, "description": "singer", "country": "United States"},
    {"name": "Zendaya", "follower_count": 185, "description": "actress", "country": "United States"},
    {"name": "Kevin Hart", "follower_count": 180, "description": "comedian", "country": "United States"},
    {"name": "Cardi B", "follower_count": 165, "description": "rapper", "country": "United States"},
    {"name": "LeBron James", "follower_count": 160, "description": "basketball player", "country": "United States"},
    {"name": "Shakira", "follower_count": 155, "description": "singer", "country": "Colombia"},
    {"name": "Demi Lovato", "follower_count": 150, "description": "singer", "country": "United States"},
    {"name": "Rihanna", "follower_count": 148, "description": "singer and entrepreneur", "country": "Barbados"},
    {"name": "Real Madrid", "follower_count": 175, "description": "football club", "country": "Spain"},
    {"name": "FC Barcelona", "follower_count": 140, "description": "football club", "country": "Spain"},
    {"name": "NASA", "follower_count": 100, "description": "space agency", "country": "United States"},
    {"name": "Emma Watson", "follower_count": 74, "description": "actress", "country": "United Kingdom"},
    {"name": "Chris Hemsworth", "follower_count": 60, "description": "actor", "country": "Australia"},
    {"name": "Tom Holland", "follower_count": 67, "description": "actor", "country": "United Kingdom"},
    {"name": "Billie Eilish", "follower_count": 125, "description": "singer", "country": "United States"},
    {"name": "Drake", "follower_count": 145, "description": "rapper", "country": "Canada"},
    {"name": "MrBeast", "follower_count": 70, "description": "YouTuber", "country": "United States"},
    {"name": "David Beckham", "follower_count": 90, "description": "former footballer", "country": "United Kingdom"},
    {"name": "Gigi Hadid", "follower_count": 77, "description": "model", "country": "United States"},
    {"name": "Zlatan Ibrahimović", "follower_count": 64, "description": "former footballer", "country": "Sweden"},
    {"name": "Gal Gadot", "follower_count": 110, "description": "actress", "country": "Israel"},
    {"name": "Chris Evans", "follower_count": 20, "description": "actor", "country": "United States"},
    {"name": "Margot Robbie", "follower_count": 31, "description": "actress", "country": "Australia"},
    {"name": "Lewis Hamilton", "follower_count": 40, "description": "Formula 1 driver", "country": "United Kingdom"},
    {"name": "Novak Djokovic", "follower_count": 17, "description": "tennis player", "country": "Serbia"},
    {"name": "Roger Federer", "follower_count": 13, "description": "former tennis player", "country": "Switzerland"},
    {"name": "Serena Williams", "follower_count": 18, "description": "former tennis player", "country": "United States"},
    {"name": "Gordon Ramsay", "follower_count": 18, "description": "chef", "country": "United Kingdom"},
    {"name": "Jamie Oliver", "follower_count": 10, "description": "chef", "country": "United Kingdom"},
    {"name": "Spotify", "follower_count": 12, "description": "music streaming service", "country": "Sweden"}
]

logo = """
  _   _ _       _               
 | | | (_) __ _| |__   ___ _ __ 
 | |_| | |/ _` | '_ \ / _ \ '__|
 |  _  | | (_| | | | |  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|   
 | |    __|___/    _____ _ __   
 | |   / _ \ \ /\ / / _ \ '__|  
 | |__| (_) \ V  V /  __/ |     
 |_____\___/ \_/\_/ \___|_|     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

person_a_num = r.randint(0,49)
person_b_num = r.randint(0,49)
new_score = 0
high_scores = []

#clear_output(wait=False) clearing

def if_same(person_a_num, person_b_num):
    """Making sure we don't have same person"""
    if person_a_num == person_b_num:
        person_b_num = r.randint(0,49)
    return person_b_num

def UI():
    """Priting the People"""
    print(logo)
    print(f"Compare A: {data[person_a_num]['name']}, {data[person_a_num]['description']}, {data[person_a_num]['country']}")
    print(vs)
    print(f"Compare B: {data[new_person_b_num]['name']}, {data[new_person_b_num]['description']}, from {data[new_person_b_num]['country']}")

def game(new_score, still_in_game):
    """Game"""
    try:
        choice = input("Please select A or B: ").upper()

        if choice not in ["A", "B"]:
            raise ValueError("Invalid choice.")

    except ValueError:
        print("You have typed in invalid letter. Please provide A or B.")
        choice = input("Please Select A or B")
    
    more_followers = max(int(data[person_a_num]['follower_count']),int(data[new_person_b_num]['follower_count']))
    
    if more_followers == int(data[person_a_num]['follower_count']):
        correct = "A"
    else:
        correct = "B"
    
    if correct == choice:
        new_score += 1
        print(f"Yes! Your current score: {new_score}")
    else:
        print(f"Nope :<. You scored: {new_score}")
        still_in_game = False
        new_score += 0
    return [new_score, still_in_game]

def high_scores_print(name, new_score, high_scores):
    high_scores.append((name, new_score))
    n = len(high_scores)
    for i in range(n-1):
      for j in range(n-i-1):
        if high_scores[j][1] > high_scores[j+1][1]:
          high_scores[j], high_scores[j+1] = high_scores[j+1], high_scores[j]

    print(high_scores[::-1])

another_try_Boolean = True

while another_try_Boolean == True:    
    print(logo)
    print("Welcome to the Game!")
    name = input("What's your name?")
    clear_output(wait=False)
    still_in_game = True 
    while still_in_game == True:
        person_a_num = r.randint(0,49)
        person_b_num = r.randint(0,49)
        person_b_num = if_same(person_a_num, person_b_num)
        new_person_b_num = person_b_num
        UI()
        new_score, still_in_game = game(new_score, still_in_game)
        t.sleep(3)
        clear_output(wait=True)
    high_scores_print(name, new_score, high_scores)
    another_try = input("Would you like to try once again? Y/N").upper()
    new_score = 0
    if another_try == "N":
        another_try_Boolean = False
else:
    print("Thanks for the game")
