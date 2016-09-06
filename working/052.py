def testMult(num, mux):
	return num * mux

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

potato = True

num = 125875
counter = 0

while potato:
	if sum_digits(num) == sum_digits(testMult(num, 2)):
		if sum_digits(num) == sum_digits(testMult(num, 3)):
			if sum_digits(num) == sum_digits(testMult(num, 4)):
				if sum_digits(num) == sum_digits(testMult(num, 5)):
					if sum_digits(num) == sum_digits(testMult(num, 6)):
						potato = False
	num += 1
print(num - 1)

#answer 142857
