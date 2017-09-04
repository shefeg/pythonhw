import random


def game(a, b):
    x = random.randint(a, b)
    inp = raw_input('Please enter your value: ')
    while int(inp) != int(x):
        print "Try again"
        game(a, b)
    else:
        print "Congratulations! You've guessed the number"
        return


game(1, 5)
