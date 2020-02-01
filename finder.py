from operator import attrgetter, itemgetter
from itertools import groupby
import random

__colors__ = ("RED", "BLUE", "YELLOW", "BLACK")

class card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return self.color + str(self.number)

class combo:
    def __init__(self, type, list):
        self.type = type
        self.list = list

def allColorLinear(cards):
    sortedCards = sorted(cards,key=attrgetter('number'))

    vaildLongestCombo = []
    for _, group in groupby(enumerate(sortedCards), lambda x: x[1].number - x[0]):
        group = list(map(itemgetter(1), group))
        if len(group) >= 3:
            vaildLongestCombo.append(group)

    allVaildCombo = []
    for combo in vaildLongestCombo:
        for length in range(3, len(list(combo)) + 1):
            for start in range(0,len(list(combo))-length + 1):
                allVaildCombo.append((combo[start:start+length]))

    return allVaildCombo
    


def findAllLinear(cards):
    possible = [allColorLinear(i) for _,i in groupby(sorted(cards,key=attrgetter('color')),lambda x: x.color)]
    return possible

def allSameColor(cards):
    cards = list(cards)
    if(len(cards) == 3):
        return [cards]
    
    elif(len(cards) == 4):
        allVaildCombo = [cards]
        for i in range(4):
            allVaildCombo.append(cards[:i]+cards[i+1:])
        return allVaildCombo
            
    return []

def findAllColor(cards):
    possible = [allSameColor(i) for _,i in groupby(sorted(cards, key=attrgetter('number')), lambda x: x.number)]
    vaild = []
    for i in possible:
        if i:
            vaild.append(i)
    return possible



test = [card(random.choice(__colors__),random.randrange(1,14)) for i in range(30)]
for i in test:
    print(i,end=' ')
print("\n\n\n\n")
for i in findAllLinear(test):
    for j in i:
        for k in j:
            print(k,end=' ')
        print()

print()
print()
print()
print()

# test = [card(col,num) for num in range(1,5) for col in __colors__]
for i in test:
    print(i,end=' ')
print("\n\n\n\n")
for i in findAllColor(test):
    for j in i:
        for k in j:
            print(k,end=' ')
        print()
