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

def isPerfect(n):
	if arrSum(divisors(n)) == n:
		return True
	else:
		return False

print(isPerfect(28))
