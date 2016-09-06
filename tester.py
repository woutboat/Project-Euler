#142857

num = 142857

def testMult(num, mux):
	return num * mux

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

print(sum_digits(num) == sum_digits(testMult(num, 2)))
