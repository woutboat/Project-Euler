def primeFind(number):
	oldnum = number
	factor = 1
	while number > 1:
		factor += 1
		if number % factor == 0:
			if 1 < factor < oldnum:
				return False # is not prime
			number //= factor
	return True # is prime!

def checkLeft(number):
	

for i in range(8, 500000):
	if primeFind(i):
