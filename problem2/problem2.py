#We need to track 2 numbers which start as 1 and 2.
x = 1
y = 2
fibsum = 0 # track total sum of even fib terms
while x <= 4000000 and y <= 4000000: 
	if y % 2 == 0:
		#print str(y) + " is even"
		fibsum = fibsum + y
	if x % 2 == 0:
		#print str(x) + " is even" 	
		fibsum = fibsum + x
	print "x:" + str(x), "y:" + str(y), "fibSum:" + str(fibsum)
	x = x + y
	y = y + x
	pass