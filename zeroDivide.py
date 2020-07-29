#Here it prints all because it is running a block not just the prints
#def spam(divideBy):
#    try:
#        return 42 / divideBy
#    except ZeroDivisionError:
#        print('Error: Invalid argument.')
#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))


#In this one print 1 doesn't happen becuase once it ifnd the error it doesn't return to try again
def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')