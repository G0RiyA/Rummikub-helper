import random as r

def Gameset(card):
    hand = r.sample(card,28)
    ai = hand[:15]
    player = hand[15:]

    
    return ai, player
    

def Cardset():
    orange = ["orange" + str(i) for i in range(1,14)]
    red = ["red" + str(i) for i in range(1,14)]
    black = ["black" + str(i) for i in range(1,14)]
    blue = ["blue" + str(i) for i in range(1,14)]
    
    return orange*2 + red*2 + black*2 + blue*2 + ["joker"]*2


def cardret():
    card = Cardset()
    ai, player = Gameset(card)
    return player

