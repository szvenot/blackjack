import random
from tkinter import Y

card_symbols = ['Diamond','Heart','Spades','Club']
card_values = ['2', '3', '4', '5', '6', '7','8','9','10','J','D','K','A']

def deck_creation(x,y):
    poker_deck = []
    for i in x:
        for j in y:
            poker_deck.append(i + " " + j)
    return poker_deck

def deal_two(deck):
    random.shuffle(deck)
    global dealt
    dealthere = []
    dealt = dealthere
    global used
    usedhere = []
    used = usedhere
    for i in range(0, (num_of_plyrs+1)*2, 2):
        dealt.append(deck[i:i + 2])
        usedhere.append(deck[i])
        usedhere.append(deck[i+1])
    return dealt

#def if_used(j,deck):
#    random.shuffle(deck)
 #   for i in range(1):
  #      if i in used:
 #           return if_used(j,deck) 
 #       else:    
 #           j.append(deck[i])
 #           deck.remove(i)
 #           print(j)
  #      return hit(j,deck)

deck = deck_creation(card_symbols,card_values)
num_of_plyrs = int(input("Give me the number of players"))
deal = deal_two(deck)
print(deal)




def hit(j,deck):
    if_fold = input("Do you wanr a hit?")
    if if_fold == "y":
        random.shuffle(deck)
        for i in range(1):
            j.append(deck[i])
            print(j)
            deck.remove(deck[i])
            return hit(j,deck)
    elif if_fold == "n":
        return j
    else:
        print("Quiet joking")
        return hit(j,deck1)

for i in used:
    if i in deck:
        deck.remove(i)

for pairs in deal:
    hit(pairs,deck)


