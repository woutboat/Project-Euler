#distinct answers for a^b where 2 <= a <= 100 and 2 <= b <= 100

numbers = []

for a in range(2,101):
	for b in range(2,101):
		print(str(a) + " " + str(b))
		numbers.append(a ** b)

print("Removing repeats")

numbers = sorted(set(numbers))

print(str(len(numbers)))

#Answeer 9183
