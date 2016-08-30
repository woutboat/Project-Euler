#Find the smallest number evenly divisible by all numbers from 1-20

potat = True
bu = 2521
while potat:
    for i in range(1,21):
        if not bu % i == 0:
