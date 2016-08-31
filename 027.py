import time

def primeFind(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        if number % factor == 0:
            if 1 < factor < oldnum:
                print("Returned False")
                return False # is not prime
            number //= factor
    return True # is prime!

def count(numa, numb):
    su = 0
    n = 0
    tmp = 0
    potat = True
    while potat == True:
        tmp = (n ** 2) + (numa * n) + numb
        if primeFind(abs(tmp)) == True:
            print(su)
        else:
            potat = False
            print("MADE FALSE")
            time.sleep(1)
        su = su + 1
    for poo in range(0, 1000):
        tmp = (poo ** 2) + (numa * poo) + numb
    return(su)

ma = 0
ars = 0
holder = 0

for i in range(-1000,1001):
    for o in range(-1000,1001):
        print("Checking: " + str(i) + ", " + str(o))
        ars = count(i,o)
        if ars > ma:
            ma = ars
            holder = i * o

print(holder)