number = 2 ** 1000
print(number)
strr = str(number)
su = 0
for i in range(0, len(strr)):
    su = su + int(strr[i])
    print(su)

print(su)