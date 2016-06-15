def median(items):
    medianNum = 0
    items = sorted(items)
    print(items)
    if len(items) % 2 == 0:
        half = int(len(items)/2)
        print(half)
        one = items[half]
        print(one)
        two = items[half - 1]
        print(two)
        medianNum = (float(one + two))/2.0
    else:
        medianNum = items[len(items)/2]
    return medianNum
print(median([4,5,5,4]))