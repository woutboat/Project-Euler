def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

ma = 0
tmp = 0
tmp2 = 0
for a in range(0,100):
    for b in range(0,100):
        tmp = a ** b
        tmp2 = sum_digits(tmp)
        print("Checking: " + str(a) + "^" + str(b) + ". Sum: " + str(tmp))
        if tmp2 > ma:
            ma = tmp2

print(ma)