counter = 5
term1 = 3
term2 = 5
term3 = 5

while len(str(term3)) < 1000:
    counter += 1
    term3 = term2 + term1
    term1 = term2
    term2 = term3
    print("Fibonacci number: " + str(counter) + ", is: " + str(term3) + ". It is " + str(len(str(term3))) + " digits long.")