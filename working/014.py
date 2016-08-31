def chain(num):
    cu = 0
    while not num == 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1
        cu += 1
    return(cu)

manum = 0
machain = 0
tmp = 0

for i in range(1, 1000001):
    tmp = chain(i)
    print("Checking: " + str(i) + ". Length: " + str(tmp))
    if tmp > machain:
        machain = tmp
        manum = i

print(manum)