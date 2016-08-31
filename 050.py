def primeFind(number):
    oldnum = number
    factor = 1
    while number > 1:
        factor += 1
        if number % factor == 0:
            if 1 < factor < oldnum:
                return False # is not prime
            number //= factor
    return True # is prime!

su = 2
num = 3
ma = 0
while su < 99:
    print(num)
    if primeFind(num) == True:
        su = su + num
        if primeFind(su) == True:
            ma = su
    num += 1

print(su)
print(ma)