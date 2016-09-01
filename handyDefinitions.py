def checkOdd(num):
    butt = True
    for i in range(0,len(str(num))):
        if int(str(num)[i]) % 2 == 0:
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

def is_pandigital(nr, n):
    nr = str(nr)
    beg=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True

def F(n):
    print(n)
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def counter(n):
    if n > 0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n))+2

    return digits

def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
