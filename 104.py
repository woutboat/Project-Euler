import math

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

#541
print("Ehh")
number = F(541)
print("blehh")
print(number)
print(counter(number))