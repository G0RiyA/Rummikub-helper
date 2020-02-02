import random as r

# make rummykub card
def Makecard():
    orange = ["orange" + str(i) for i in range(1,14)]
    red = ["red" + str(i) for i in range(1,14)]
    black = ["black" + str(i) for i in range(1,14)]
    blue = ["blue" + str(i) for i in range(1,14)]
    
    return orange*2 + red*2 + black*2 + blue*2 + ["joker"]*2

# choice random card
def Gameset(cards):
    hand = []
    for i in range(14):
        card = r.choice(cards)
        hand.append(card)
        cards.remove(card)

    return hand, cards

# card drow
def Drow(cards):
    card = r.choice(cards)
    cards.remove(card)

    return card, cards

# set rummykub
def Cardset():
    cards = Makecard()
    hand, cards = Gameset(cards)
    return hand, cards


