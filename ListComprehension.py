def evenList(numbers):
    newList = [x for x in numbers if x % 2 == 0]
    return newList

print(evenList([2, 3, 5, 90, 12, 56, 77, 79, 43, 21]))