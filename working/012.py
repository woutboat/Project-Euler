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
tmp2 = 0

while potato:
	tmp = triNumber(num)
	tmp2 = len(factors(tmp))
	if tmp2 > 500:
		potato = False
		print(num)
		print("Found number of factors - " + str(tmp2))
		print(tmp)
	else:
		tmp = 0
		tmp2 = 0
		num += 1

#Answer: 76576500
