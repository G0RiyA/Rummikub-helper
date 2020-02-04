from operator import attrgetter, itemgetter
from itertools import groupby
import random

__colors__ = ("red", "blue", "orange", "black")
possible = {}
memo = {}

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
    
    def __str__(self):
        return self.color + str(self.number)

    def __eq__(self, other):
        return (isinstance(other, type(self))) and\
            (self.color, self.number) ==\
                (other.color, other.number)

    def __hash__(self):
        return hash(self.color)^hash(self.number)^  hash((self.color, self.number))
    
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
    # print(vaildLongestCombo)

    allVaildCombo = []
    for combo in vaildLongestCombo:
        for length in range(3, min(len(list(combo)) + 1, 6)):
            for start in range(0,len(list(combo))-length + 1):
                allVaildCombo.append(combo[start:start+length])

    # print(allVaildCombo)

    return allVaildCombo
    


def findAllLinear(cards):
    possible = [allColorLinear(i) for _,i in groupby(sorted(cards,key=attrgetter('color')),lambda x: x.color)]
    # print(possible)

    vaild = []
    for i in possible:
        # print(i)
        if i:
            for j in i:
                if j:
                    vaild.append(j)
    # print(vaild)
    # print('\n\n\n\n')
    return vaild

def allSameColor(cards):
    cards = list(cards)
    if(len(cards) == 3):
        return [cards]
    
    elif(len(cards) == 4):
        allVaildCombo = [cards]
        for i in range(4):
            allVaildCombo.append((cards[:i]+cards[i+1:]), )
        return allVaildCombo
            
    return []

def findAllColor(cards):
    possible = [allSameColor(i) for _,i in groupby(sorted(cards, key=attrgetter('number')), lambda x: x.number)]
    vaild = []
    for i in possible:
        if i:
            for j in i:
                if j:
                    vaild.append(j)
    return vaild

def findAllCases(combos, hands, tables):
    global memo
    allCards = tuple(set(list(set(hands)) + list(set(tables))))
    if len(allCards) == 0:
        return (0,combos)
    
    if allCards in memo:
        return memo[allCards]

    # print(len(combos))
    score = 0
    # for card in hands:
    #     print(score,end=' ')
    #     score += card.number
    # print(score)

    if len(allCards) < 3:
        return (score, combos)

    a,b=findAllColor(allCards),findAllLinear(allCards)
    allCombos=a+b

    if len(allCombos) == 0:
        return (score, combos)

    resultCombos = combos.copy()

    # print(allCombos)

    for combo in allCombos:
        # print(combo)
        if len(combo) == 0:
            continue

        newHands = []
        newTables = []
        cb = combo.copy()

        for i in tables:
            if i in cb:
                cb.remove(i)
            else:
                newTables.append(i)

        for i in hands:
            if i in cb:
                cb.remove(i)
            else:
                newHands.append(i)
        
        newAllCards = newHands.copy() + newTables.copy()


        ret = combos.copy()
        ret.append(combo)
        # print((len(newHands), len(hands)),len(cb),len(combo),len(resultCombos))
        retscore, retcombos = findAllCases(ret.copy(),newHands,newTables)
        # print(retscore,len(retcombos))
        if retscore == 0:
            return (retscore, retcombos)
        if retscore < score:
            score,resultCombos = retscore, retcombos.copy()
        # print(score,resultCombos)

    # print(len(resultCombos),100)
    memo[allCards] = (score,resultCombos)
    return memo[allCards]
                

def solver(hands, tables):
    global memo
    memo = {}
    score, combos = findAllCases([], hands, tables)
    memo = {}
    return combos





test = [Card(__colors__[0],i) for i in range(1,4)] + [Card('black',3),Card('blue',3)]
test += [Card('orange',i) for i in range(5,9)]
# for i in test:
#     print(i,end=' ')
# print("\n\n\n\n")
# for i in findAllLinear(test):
#     for j in i:
#         print(j,end=' ')
#     print()

# print('\n\n\n\n')

# test = [card(col,num) for num in range(1,5) for col in __colors__]
# for i in test:
#     print(i,end=' ')
# print("\n\n\n\n")
# for i in findAllColor(test):
#     for j in i:
#         print(j,end=' ')
#     print()

# print('\n\n\n\n')

for i in solver(test,[]):
    for j in i:
        print(j,end=' ')
    print()