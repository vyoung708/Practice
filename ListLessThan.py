def listLess(a_list):
    newList = [num for num in a_list if num < 5]
    if input("Would you like to find all numbers less than a specific number?(y/n): ") == "y":
        limit = int(input("Enter that number: "))
        newList = [num for num in a_list if num < limit]
    return newList
print(listLess([2, 3, 7, 9, 4, 6, 5, 7, 33, 55, 99, 12]))