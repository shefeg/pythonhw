from __future__ import print_function


def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end='')


convertToBinary(42)
