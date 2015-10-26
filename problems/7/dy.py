def factor(n):
	if n==1: return [1]
	i = 2
	limit = n**0.5		# max root of n
	while i<=limit:
		if n%i == 0:	# if i is divisor of n
			return False 	# return ret!
		i += 1

	return [n]			# if n is prime, return that(base case)

def isPrime(n):
	if not factor(n):	return False
	else:	return True

primeCounter = 0
targetPrime = 0
i = 2

while True:
	if isPrime(i):
		primeCounter += 1
		print("%d, %d" %(i, primeCounter)) 
		if primeCounter == 10001:
			targetPrime = i
			break
	i += 1

print(targetPrime)