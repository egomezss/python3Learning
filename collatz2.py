def collatz():
    global number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)


try:
    print('Hi, please type an integer number')
    number = int(input())
except ValueError:
    print('Sorry, that is not an integer, please type again')
    number = int(input())

collatz()
