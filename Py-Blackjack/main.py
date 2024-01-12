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

def deal_card():
    return random.choice(cards)
# print(deal_card())

for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
# print(f"user: {user_cards}")
# print(f"dealer: {dealer_cards}")

def calculate_score(cards_lists):
    if sum(cards_lists) == 21 and len(cards_lists) == 2:
        return 0
    if 11 in cards_lists and sum(cards_lists) > 21:
        cards_lists.remove(11)
        cards_lists.append(1)

    return sum(cards_lists)
# print(calculate_score(user_cards))

