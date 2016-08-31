def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

tmp = "tmp"
su1 = 0
numbers = []
for i in range(3, 1000001):
    su1 = 0
    print("Checking " + str(i))
    tmp = str(i)
    for o in range(0,len(tmp)):
        su1 = su1 + factorial(int(tmp[o]))
    if su1 == i:
        numbers.append(i)

print(numbers)

su2 = 0

for x in range(0,len(numbers)):
    su2 = su2 + int(numbers[x])

print(su2)