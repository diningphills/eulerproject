def factor(n):
  if n==1: return [1]
  i = 2
  limit = n**0.5    # max root of n
  while i<=limit:
    if n%i == 0:  # if i is divisor of n
      return False  # return ret!
    i += 1
  return [n]      # if n is prime, return that(base case)

def isPrime(n):
  if n==1 or not factor(n): return False
  else: return True


def getRightSet(n):
  result = set()
  while(n>10):
    n = n/10
    result.add(n)
  return result

def getLeftSet(n):
  result = set()
  a = 10
  while(n%a != n):
    result.add(n%a)
    a = a*10
  return result


def prime_test(n):
  right = getRightSet(i)
  left = getLeftSet(i)
  union = right | left
  for n in union:
    if not isPrime(n): return False
  return True

answer = set()


for i in range(10, 1000000):
  if isPrime(i) and prime_test(i):
    answer.add(i)


print answer
print sum(answer)