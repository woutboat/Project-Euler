#Find the sum of even valued Fibonacci terms below four million.

term1 = 1
term2 = 2
term3 = 0
sums = 0
while term3 < 4000000:
    print("TERM -- " + str(term3))
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    if (term3 % 2 == 0) and (term3 < 4000000):
        sums = sums + term3

print(term3)
print(sums)

#Answer: 4613732