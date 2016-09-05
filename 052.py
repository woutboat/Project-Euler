def testMult(num, mux):
	return num * mux

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

potato = True

num = 1
counter = 0

while potato:
	for i in range(2,7):
		if sum_digits(num) == sum_digits(testMult(num, i)):
			counter += 1
	if counter == 6:
		potato = False
	else:
		num += 1

print(num)
