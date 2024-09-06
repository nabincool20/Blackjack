import random

# Cards list as per the house rules
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal a random card from the deck
def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

# Function to calculate the score of the hand
def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    # Check for a blackjack (2 cards: ace and a 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 will represent a blackjack
    # Check if the hand has an ace (11). If the score is over 21, count the ace as 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare the scores of user and computer
def compare(user_score, computer_score):
    """Compares the user and computer scores and returns the result."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Main function to play the game
def play_game():
    print("#################### Blackjack ####################")
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    # Deal initial cards to user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        # Check for blackjack or if user has gone over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Once the user is done, the computer should draw cards if its score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop to ask the user if they want to restart
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
