#get user input
user_input = input("Enter three numbers with spaces in between them: ")
#split user input on spaces
inputItems = user_input.split()
#list for numbers
numbers = []
#cast each string in inputItems to an int and store in numbers
for one in inputItems:
    numbers.append(int(one))
#take the maximum of three numbers
def max_of_three(numberList):
    highest = 0
    for num in numberList:
        if num > highest:
            highest = num
    return highest
#test
print(max_of_three(numbers))
