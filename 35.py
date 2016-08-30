def toString(List):
    return ''.join(List)

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
        if not primeFind(int(toString(a))):
            potat = False
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

def checkOdd(num):
    butt = True
    for i in range(0,len(str(num))):
        if int(str(num)[i]) % 2 == 0:
            butt = False
    if butt:
        return True
    else:
        return False

string = "1"
n = len(string)
a = list(string)
permute(a, 0, n-1)

print(su)

numbers = []

for i in range(2,1000001):
    print("Checking: " + str(i))
    su = 0
    string = i
    n = len(str(string))
    a = list(str(string))
    if checkOdd(i):
        permute(a, 0, n-1)
        if potat:
            numbers.append(i)
    potat = True

print(numbers)
print(len(numbers))

