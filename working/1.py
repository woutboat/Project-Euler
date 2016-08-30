#Find the sum of all multiples of 3 or 5 below 1000

sum = 0
for x in range(3,1000):
    print(x)
    if (x % 3 == 0) or (x % 5 == 0):
        sum = sum + x
        print(" SUM  -- " + str(sum))

print(sum)

#Answer: 233168