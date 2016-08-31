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

num = 4
counter = 2
prime = True
while counter <= 10000:
    if primeFind(num) == True:
        counter += 1
        print("Prime number: " + str(counter) + ", is: " + str(num))
    num += 1
