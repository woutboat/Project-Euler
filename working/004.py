tmp = 0
ma = 0
for x in range(0,1000):
    for i in range(0,1000):
        print(str(x) + " x " + str(i))
        tmp = x * i
        if (str(tmp) == str(tmp)[::-1]) and (tmp > ma):
            ma = tmp

print(ma)