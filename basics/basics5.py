import time

def histogram(number):
    for i in number:
        list = ['*'] * i
        print (''.join(list) + "\n")
        time.sleep(1)

histogram ([4, 9, 7])
