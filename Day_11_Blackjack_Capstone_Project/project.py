import random as r 
cards = [
    "A", 2, 3, 4, 5, 6, 7,
    8, 9, 10, "J", "Q", "K"
]

cards_P = [
    "A", 2, 3, 4, 5, 6, 7,
    8, 9, 10, "J", "Q", "K"
]

cards_PC = [
    "A", 2, 3, 4, 5, 6, 7,
    8, 9, 10, "J", "Q", "K"
]

card = r.choice(cards)
player_hand = []
computer_hand = []
player_score = 0

print('Welcome to Blackjack!')
version = int(input("How many decks are there? 1 for 2(1) / 1 per person (2) / infinite (3)"))

if version == 3:
    def draw_another():
        """Draws another card"""
        card = r.choice(cards)
        player_hand.append(card)
        
    def start_game():
        """Function to start a game"""
        for i in range(2):
            card = r.choice(cards)
            player_hand.append(card)
            card = r.choice(cards)
            computer_hand.append(card)
        return [player_hand, computer_hand]
        
    def computer_gambling(computer_score_2):
        if computer_score_2 < 11:
            card = r.choice(cards)
            computer_hand.append(card)
        elif computer_score_2 <= 15 and r.random() <= 0.9:
            card = r.choice(cards)
            computer_hand.append(card)
        elif computer_score_2 == 16 and r.random() <= 0.6:
            card = r.choice(cards)
            computer_hand.append(card)
        elif computer_score_2 == 17 and r.random() <= 0.2:
            card = r.choice(cards)
            computer_hand.append(card)
        else:
            print("Computer stands for now")
            
elif version == 2:
    def draw_another():
        """Draws another card"""
        card = r.choice(cards_P)
        player_hand.append(card)
        cards_P.remove(card)
    
    def start_game():
        """Function to start a game"""
        for i in range(2):
            card = r.choice(cards_P)
            player_hand.append(card)
            cards_P.remove(card)
            card = r.choice(cards_PC)
            computer_hand.append(card)
            cards_PC.remove(card)
        return [player_hand, computer_hand]
        
    def computer_gambling(computer_score_2):
        if computer_score_2 < 11:
            card = r.choice(cards_PC)
            computer_hand.append(card)
            cards_PC.remove(card)
        elif computer_score_2 <= 15 and r.random() <= 0.9:
            card = r.choice(cards_PC)
            computer_hand.append(card)
            cards_PC.remove(card)
        elif computer_score_2 == 16 and r.random() <= 0.6:
            card = r.choice(cards_PC)
            computer_hand.append(card)
            cards_PC.remove(card)
        elif computer_score_2 == 17 and r.random() <= 0.2:
            card = r.choice(cards_PC)
            computer_hand.append(card)
            cards_PC.remove(card)
        else:
            print("Computer stands for now")

elif version == 1:
    def draw_another():
        """Draws another card"""
        card = r.choice(cards_P)
        player_hand.append(card)
        cards_P.remove(card)
    
    def start_game():
        """Function to start a game"""
        for i in range(2):
            card = r.choice(cards_P)
            player_hand.append(card)
            cards_P.remove(card)
            card = r.choice(cards_P)
            computer_hand.append(card)
            cards_P.remove(card)
        return [player_hand, computer_hand]
        
    def computer_gambling(computer_score_2):
        if computer_score_2 < 11:
            card = r.choice(cards_P)
            computer_hand.append(card)
            cards_P.remove(card)
        elif computer_score_2 <= 15 and r.random() <= 0.9:
            card = r.choice(cards_P)
            computer_hand.append(card)
            cards_P.remove(card)
        elif computer_score_2 == 16 and r.random() <= 0.6:
            card = r.choice(cards_P)
            computer_hand.append(card)
            cards_P.remove(card)
        elif computer_score_2 == 17 and r.random() <= 0.2:
            card = r.choice(cards_P)
            computer_hand.append(card)
            cards_P.remove(card)
        else:
            print("Computer stands for now")

def calc_the_score(player_hand):
    """Calculates the current score"""
    player_score = 0
    for card in player_hand:
        if card == "J" or card == "Q" or card == "K":
            player_score += 10
        elif card == "A":
            player_score += 11
        else:
            player_score += card
    return player_score

def calc_the_score_c(computer_hand):
    """Calculates the Computer's current score"""
    computer_score = 0
    for card in computer_hand:
        if card == "J" or card == "Q" or card == "K":
            computer_score += 10
        elif card == "A":
            computer_score += 11
        else:
            computer_score += card
    return computer_score

def show_down(computer_score, player_score):
    """Finishing the Game"""
    print(f"Computer's current score is: {calc_the_score_c(computer_hand)} and hand {(computer_hand)}")
    if calc_the_score_c(computer_hand) > calc_the_score(player_hand) and calc_the_score_c(computer_hand) <= 21:
        print("You lost")
    elif calc_the_score_c(computer_hand) == calc_the_score(player_hand):
        print("Draw!")
    else:
        print("You Win!")
        

start_game()
computer_score = calc_the_score_c(computer_hand)
print(f"This is Compuetr's deck: [{computer_hand[0]},...]")

while calc_the_score(player_hand) <= 21:

    # PLAYER TURN
    print(f"Your deck: {player_hand}")
    print(f"Your score: {calc_the_score(player_hand)}")
    
    # COMPUTER TURN
    computer_score = calc_the_score_c(computer_hand)

    if computer_score < 17:
        computer_gambling(computer_score)

    computer_score = calc_the_score_c(computer_hand)

    choice = input("Would you like to draw another? ")

    if choice == "yes":
        draw_another()
    else: 
        show_down(computer_hand, player_score)
        break
else:
    print(f"You lost, overcame 21. You came up to {calc_the_score(player_hand)} ")
