# swaps symbols in the string: first symbol becomes second, second becomes third, last becomes first
def caesar_cipher(string, number):
    list = []
    ciphered = []
    for i in range(len(string)):
        if i + number <= len(string) - 1:
            list.append(i + number)
            ciphered += string[list[i]]
        else:
            list.append((i + number) - len(string))
            ciphered += string[list[i]]
    print list
    print ''.join(ciphered)


caesar_cipher('terry', -1)
