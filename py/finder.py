from operator import attrgetter, itemgetter
from itertools import groupby
import random

__colors__ = ("red", "blue", "orange", "black")
possible = {}

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
    allCards = list(set(list(set(hands)) + list(set(tables))))
    if len(allCards) == 0:
        return combos

    # print(combos)

    a,b=findAllColor(allCards),findAllLinear(allCards)
    # print(a)
    # print(b)
    allCombos=a+b
    if len(allCombos) == 0:
        return []
    
    # print(combos)

    # print(allCombos)
    # print(combos)

    # for i in combos:
    #     print(i,end=' ')
    # print(0)

    # print(allCards)
    # print(allCombos)
    # print(1)

    # for i in allCombos:
    #     for j in i:
    #         print(j,end=" ")
    #     print()
    # print(2)
    
    # print(combos)

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

        # for i in cb:
        #     print(i,end=' ')
        # print()
        for i in hands:
            if i in cb:
                # print(i,end=' ')
                cb.remove(i)
            else:
                # print(i,end=' ')
                newHands.append(i)
        # print()
        # for i in hands:
        #     print(i,end=' ')
        # print()
        
        newAllCards = newHands + newTables
        
        # print(newAllCards == hands+tables)

        if 0 < len(newAllCards) < 3:continue
        # for i in combos:
        #     for j in i:
        #         print(j,end=' ')
        #     print()
        # print(combos)
        ret = combos.copy()
        ret.append(combo)
        result = findAllCases(ret,newHands,newTables)
        if result: return result
    # print(result)
    return []
                

def solver(hands, tables):
    result = findAllCases([], hands, tables)
    return result





# test = [card(__colors__[i%3],i//3+1) for i in range(9)]
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

# for i in solver(test,[]):
#     for j in i:
#         print(j,end=' ')
#     print()