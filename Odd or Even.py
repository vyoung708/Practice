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
print(evenorodd())