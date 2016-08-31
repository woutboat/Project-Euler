arr = []
for i in range(2,500000):
    su = 0
    print(i)
    for x in range(0,len(str(i))):
        su = su + ( int(str(i)[x]) ** 5)
    if su == i:
        arr.append(i)

print(arr)