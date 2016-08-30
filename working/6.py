su = 0
for i in range(0,100):
    su = su + ((i + 1) * (i + 1))
    print(su)

su2 = 0
for x in range(0,100):
    su2 = su2 + (x + 1)
su2 = su2 * su2
print(su2)

print(str(su2) + " -- " + str(su))

print(su2 - su)