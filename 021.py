def divisors(n):
	potat = []
	for i in range(1, n):
		if n % i == 0:
			potat.append(i)
	return potat

def arrSum(arr):
	su = 0
	for i in range(0,len(arr)):
		su += arr[i]
	return su

def a(n):
	return arrSum(divisors(n))

def b(n):
	return arrSum(divisors(n))

ehh = []

for o in range(1,10001):
	for p in range(1,o + 1):
		if a(o) == b(p):
			ehh.append(o)
			ehh.append(p)

print(arrSum(ehh))

#answer 31626
