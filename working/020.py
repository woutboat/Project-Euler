def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 100

num = factorial(num)

print("Listed Factorial: " + str(num))

stt = str(num)
su = 0

for i in range(0,len(stt)):
    su = su + int(stt[i])

print(su)