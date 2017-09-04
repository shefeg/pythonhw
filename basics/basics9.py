def check_bracket(string):
    print string
    pure_string = [x for x in string if x == '[' or x == ']']

    balance = 0
    for i in range(len(pure_string)):
        if pure_string[i] == '[':
            balance += 1
        else:
            balance -= 1
    if balance == 0:
        print "String with brackets is balanced"
    else:
        print "String with brackets is not balanced"


check_bracket("""[]
[][]
[[][]]""")
