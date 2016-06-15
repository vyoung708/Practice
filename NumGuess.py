from random import randint
def NumGuess():
    secretNum = randint(1, 9)
    userInput = ""
    guesses = 0
    while userInput != "exit":
        userInput = input("Guess a number between 1 and 9: "
        guesses += 1
        if userInput == secretNum:
            print("Correct! It took you %d guesses" % (guesses))
            break
        elif userInput > secretNum:
            print("")
