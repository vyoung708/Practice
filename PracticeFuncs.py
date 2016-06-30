import random
import datetime
import string

def Divisors():
    divide = int(input("Enter the number you want the divisors of: "))
    numbers = range(1, divide + 1)
    for num in numbers:
        if divide % num == 0:
            print(num)

def FibonacciGen( num ):
    nums = [1, 1]
    if num == 1:
        return 1
    elif num == 2:
        return nums
    else:
        for i in range(1, num-1):
            nums.append(nums[i] + nums[i-1])
        return nums

def evenList(numbers):
    newList = [x for x in numbers if x % 2 == 0]
    return newList

def getListEnds( list ):
    newList = [list[0], list[len(list)-1]]
    return newList

def listLess(a_list):
    newList = [num for num in a_list if num < 5]
    if input("Would you like to find all numbers less than a specific number?(y/n): ") == "y":
        limit = int(input("Enter that number: "))
        newList = [num for num in a_list if num < limit]
    return newList

def ListOverlap(list1, list2):
    newList = list((set(list1).intersection(set(list2))))
    return newList

def randList(length, num):
    yourList = []
    for i in range(length):
        yourList.append(random.randint(0, num))
    return yourList

def max_of_three(numberList):
    highest = 0
    for num in numberList:
        if num > highest:
            highest = num
    return highest

def NumGuess():
    secretNum = random.randint(1, 9)
    userInput = ""
    guesses = 0
    while userInput != "exit":
        userInput = input("Guess a number between 1 and 9: ")
        userInput = int(userInput)
        guesses += 1
        if userInput == secretNum:
            print("Correct! It took you %d guesses" % (guesses))
            break
        elif userInput > secretNum:
            print("Your answer was too high!")
        else:
            print("Your answer was too low")

def evenorodd():
    try:
        number = int(input("Please enter a number to check: "))
        divide = int(input("Please enter a number to divide by: "))
        if number % divide == 0:
            return "%d goes evenly into %d" % (number, divide)
        elif number % 4 == 0:
            return "this number is a multiple of 4"
        elif number % 2 == 0:
            return "%d is even" % (number)
        elif number % 2 != 0:
            return "%d is odd" % (number)
        else:
            return "I don't know"
    except ValueError:
        print("You did not enter a number")
        evenorodd()

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

def RockPaperScissors():
    winner = False
    nameOne = input("What is the first player's name?: ")
    nameTwo = input("What is the second player's name?: ")
    playOne = ""
    playTwo = ""
    while winner != True:
        playOne = input("Enter rock, paper, or scissors: ")
        playTwo = input("Enter rock, paper, or scissors: ")
        if Compare(playOne, playTwo) == "one":
            winner = True
            print("Player one is the winner")
        elif Compare(playOne, playTwo) == "tie":
            print("There was no winner")
        elif Compare(playOne, playTwo) == "two":
            winner = True
            print("Player two is the winner")
        else:
            print("You done messed up")

def Compare(one, two):
    if one == "rock" and two == "scissors":
        return "one"
    elif one == two:
        return "tie"
    elif one == "scissors" and two == "paper":
        return "one"
    elif one == "paper" and two == "rock":
        return "one"
    else:
        return "two"

def Palindrome():
    words = input("Please enter a string: ")
    if words == words[::-1]:
        return True
    else:
        return False

def turn100():
    name = input("Please enter your name: ")
    now = datetime.datetime.now()
    cien_year = 0
    print_num = 1
    age = int(input("Please enter your age: "))
    print_num = int(input("Enter another number: "))
    cien_year = now.year + (100-age)
    for i in range(print_num):
        print("%s will turn 100 in the year %d" % (name, cien_year))

def remDupSets( items ):
    new_list = set(items)
    items = list(new_list)
    return items

def remDupOther( items ):
    new_items = []
    for i in range(0, len(items)):
        if items[i] not in new_items:
            new_items.append(items[i])
    return new_items

def reverseSentence( words ):
    all_words = words.split()
    all_words = all_words[::-1]
    return " ".join(all_words)

def passwordGen( length ):
    password = []
    symbols = ['!', '?', "@", '_', '-', '/', '(', ')']
    letters = []
    for item in string.ascii_letters:
        letters.append(item)
    for i in range(length):
        listNum = random.randint(0, 3)
        if listNum == 1:
            password.append(symbols[random.randint(0, len(symbols) - 1)])
        elif listNum == 2:
            password.append(letters[random.randint(0, len(letters) - 1)])
        elif listNum == 0:
            password.append(str(random.randint(0, 9)))
    return "".join(password)