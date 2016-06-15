def Divisors():
    divide = int(input("Enter the number you want the divisors of: "))
    numbers = range(1, divide + 1)
    for num in numbers:
        if divide % num == 0:
            print(num)
Divisors()