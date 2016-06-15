import datetime
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
turn100()