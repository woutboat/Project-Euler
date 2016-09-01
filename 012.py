def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triNumber(number):
	sum = 0
	for i in range(1, number + 1):
		sum = sum + i
	return sum

potato = True
num = 1
tmp = 0
tmp2 = []

while potato:
	tmp = triNumber(num)
