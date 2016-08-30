def toString(List):
    return ''.join(List)

def checkOdd(num):
    butt = True
    for i in range(0,len(str(num))):
        if int(str(num)[i]) % 2 == 0:
            butt = False
    if butt:
        return True
    else:
        return False

def checkOdd2(num):
    butt = True
    if int(num) % 3 == 0:
        butt = False
    if butt:
        return True
    else:
        return False

def checkOdd3(num):
    butt = True
    for i in range(0,len(str(num))):
        if int(str(num)[i]) % 5 == 0:
            butt = False
    if butt:
        return True
    else:
        return False

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

su = 0
potat = True

def permute(a, l, r):
    global su
    global potat
    tmp = 0
    if l==r:
        if not (checkOdd2(toString(a))):
            potat = False
        else:
            if not primeFind(int(toString(a))):
                potat = False
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

print(su)

numbers = [2,3,5]

for i in range(2,1000001):
    print("Checking: " + str(i))
    su = 0
    string = i
    n = len(str(string))
    a = list(str(string))
    if checkOdd(i) and checkOdd2(i) and checkOdd3(i):
        permute(a, 0, n-1)
        if potat:
            numbers.append(i)
    potat = True

print(numbers)
print(len(numbers))

