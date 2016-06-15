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
RockPaperScissors()