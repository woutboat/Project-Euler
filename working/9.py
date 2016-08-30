import math
marker = [1,1]
tmp = 0
for num1 in range(1,1001):
    for num2 in range(num1,1001):
        tmp = (num1 * num1) + (num2 * num2)
        tmp = tmp ** (1/2.0)
        print("Checking: " + str(num1) + " x " + str(num2) + " = " + str(tmp) + ".")
        if (tmp + num1 + num2) == 1000:
            marker[0] = num1
            marker[1] = num2

tmp = (marker[0] * marker[0]) + (marker[1] * marker[1])
tmp = tmp ** (1/2.0)
final = marker[1] * marker[0] * tmp
print(str(marker[0]) + " X " + str(marker[1]) + " X " + str(tmp) + " = " + str(final))