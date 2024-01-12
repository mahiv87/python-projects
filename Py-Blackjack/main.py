import random

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []
is_game_over = False


def deal_card():
    return random.choice(cards)


def calculate_score(cards_lists):
    if sum(cards_lists) == 21 and len(cards_lists) == 2:
        print(f"Blackjack")
        return 0

    if 11 in cards_lists and sum(cards_lists) > 21:
        cards_lists.remove(11)
        cards_lists.append(1)

    return sum(cards_lists)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "You lose, Dealer has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "Busted. You lose"
    elif dealer_score > 21:
        return "Dealer busted. You win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"

for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
# print(f"user: {user_cards}")
# print(f"dealer: {dealer_cards}")

while not is_game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Your cards: {user_cards}, Your score: {user_score}")
    print(f"Dealers first card: {dealer_cards[0]}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        should_hit = input("Type 'h' to hit, type 'p' to pass: \n")
        if should_hit == "h":
            user_cards.append(deal_card())
        else:
            print(f"Your cards: {user_cards}, Your score: {user_score}")
            print(f"Dealer cards: {dealer_cards}, Dealer score: {dealer_score}")
            is_game_over = True

while dealer_score < 17 and dealer_score != 0:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)



