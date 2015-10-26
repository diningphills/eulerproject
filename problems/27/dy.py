def factor(n):
    if n==1: return [1]
    i = 2
    limit = n**0.5      # max root of n
    while i<=limit:
        if n%i == 0:    # if i is divisor of n
            return False    # return ret!
        i += 1

    return n        # if n is prime, return that(base case)

def isPrime(n):
    if not factor(n):   return False
    else:   return n

def polynomial(n, a, b):
    return n*n + a*n + b

def testPrimeCount(a, b):
    n = 0

    while True:
        result = polynomial(n, a, b)
        result = abs(result)
        if  not isPrime(result):
            return n
        else:
            n += 1

maxPrimeCount = 0
maxA = 0
maxB = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        localPrimeCount = testPrimeCount(a, b)
        if localPrimeCount >= maxPrimeCount:
            maxPrimeCount = localPrimeCount
            maxA = a
            maxB = b


print(maxA, maxB, maxA*maxB)