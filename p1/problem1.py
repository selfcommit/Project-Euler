#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

count = 0
countmin = 0
countmax = 1000
multiplesum= 0
sentence = " "
for x in xrange(countmin,countmax):
	if (x % 3 == 0) or (x % 5 == 0):
		multiplesum = multiplesum + x
		sentence = sentence + str(x) + " + "
	pass

print sentence + " = " + str(multiplesum)