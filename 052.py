def testMult(num, mux):
	return num * mux

def sum_digits(n):
	s = 0
	while n:
		s += n % 10
		n //= 10
	return s

potato = True

num = 125874
counter = 200000

while potato:
	if sum_digits(num) == sum_digits(testMult(num, 2)):
		counter += 1
		for i in range(3,7):
			if sum_digits(num) == sum_digits(testMult(num, i)):
				counter += 1
				print(str(num) + " - " + str(counter))
	if counter == 6:
		potato = False
	else:
		num += 1
		counter = 0

print(num)
