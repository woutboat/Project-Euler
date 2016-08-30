print(bin(62512)[2:])


su = 0
for num in range(1,999999):
    if str(num) == str(num)[::-1]:
        if str(bin(num)[2:]) == str(bin(num)[2:])[::-1]:
            print(str(num) + " -- " + str(bin(num)[2:]))
            su = su + num

print(su)