#Find the smallest number evenly divisible by all numbers from 1-20

potat = True
bu = 2520
while potat:
	print(bu)
	tomat = True
	for i in range(1,21):
		if not bu % i == 0:
			tomat = False
	if tomat:
		break
	else:
		bu+=1
print bu
