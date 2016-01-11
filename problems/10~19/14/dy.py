def collatz(n):
	times = 1

	while n != 1:
		times += 1

		if n%2 == 0:	n = n/2
		else:			n = 3*n+1

	return times


	#if n==1:
	#	return 1
	#elif n%2 == 0:
	#	times += collatz(n/2, times)
	#else:
	#	times += collatz(3*n+1, times)
	#
	#return times

greatestTime = 0

for i in range(1, 1000001):
	n = 100001-i
	coll = collatz(i)
	if coll > greatestTime:
		print("%d: %d > %d" %(i, coll, greatestTime))
		greatestTime = coll

print(greatestTime)