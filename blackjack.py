import random

card_symbols = ['Diamond','Heart','Spades', 'Club']
card_values = ['2', '3', '4', '5', '6', '7','8','9','10','J','D','K','A']

def deck_creation(x,y):
    poker_deck = []
    for i in x:
        for j in y:
            poker_deck.append(i + " " + j)
    return poker_deck

def deal_two(deck):
    random.shuffle(deck)
    dealt = []
    used = []
    for i in range(0, (num_of_plyrs+1)*2, 2):
        dealt.append(deck[i:i + 2])
        used.append(deck[i])
        used.append(deck[i+1])
    return dealt, used

num_of_plyrs = int(input("Give me the number of players"))
print(deal_two(deck_creation(card_symbols,card_values)))



