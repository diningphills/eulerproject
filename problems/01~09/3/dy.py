def factor(n):
	if n==1: return [1]
	i = 2
	limit = n**0.5		# max root of n
	while i<=limit:
		if n%i == 0:	# if i is divisor of n
			ret = factor(n/i)
			ret.append(i)
			return ret 	# return ret!
		i += 1

	return [n]			# if n is prime, return that(base case)

print(factor(600851475143))