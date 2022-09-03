#import random

card_symbols = ['Diamond','Heart','Spades', 'Club']
card_values = ['2', '3', '4', '5', '6', '7','8','9','10','J','D','K','A']

def deck_creation(x,y):
    poker_deck = []
    for i in x:
        for j in y:
            poker_deck.append(i + " " + j)
    return poker_deck


print(deck_creation(card_symbols,card_values))

'''random_index = random.randint(0,len(letters)-1)

print(letters[random_index])'''