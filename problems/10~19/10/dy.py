def factor(n):
	if n==1: return [1]
	i = 2
	limit = n**0.5		# max root of n
	while i<=limit:
		if n%i == 0:	# if i is divisor of n
			return False 	# return ret!
		i += 1

	return n		# if n is prime, return that(base case)

def isPrime(n):
	if not factor(n):	return False
	else:	return n

sum = 0
n = 2

while True:
	if not factor(n):	pass
	else:
		if(n > 2000000): break
		sum += n

	n += 1

print(sum)