def ListOverlap(list1, list2):
    newList = list((set(list1).intersection(set(list2))))
    return newList

import random

def randList(length, num):
    yourList = []
    for i in range(length):
        yourList.append(random.randint(0, num))
    return yourList

print(ListOverlap(randList(10, 45), randList(10, 45)))