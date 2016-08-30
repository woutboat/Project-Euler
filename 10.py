import time

with open('primes.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

newData = data.split(' ')

su = 0

for i in range(0, len(newData)):
    if newData[i] == '':
        newData[i] = 0

print(newData)

for x in range(0, len(newData)):
    su = su + int(newData[x])
    print(su)

print(su)