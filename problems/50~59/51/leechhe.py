size = 1000000
isPrime = [True]*size
def eratosthenes(limit):
	primes = []
	for i in range(2,limit):
		if isPrime[i] :
			primes.append(i)
			j = i*i
			while j < limit :
				isPrime[j] = False
				j += i
	return primes

def isEightSet(n, p):
	cnt = 0
	for i in '0123456789':
		k = int(n.replace(p,i))
		if k > 100000 and isPrime[k]:
			cnt += 1
	return cnt == 8

for prime in eratosthenes(size):
	if prime > 100000 :
		prime = str(prime)
		if prime.count('0') == 3 and isEightSet(prime,'0') or \
		prime.count('1') == 3 and prime[-1] != '1' and isEightSet(prime,'1') or \
		prime.count('2') == 3 and isEightSet(prime,'2') :
			print(prime)
			break
