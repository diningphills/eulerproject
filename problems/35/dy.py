
# number to list
def to_list(n):
  if n < 10:
    return [n]
  else:
    result = to_list(n/10)
    result.append(n%10)
    return result

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number

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
  if not factor(n): return False
  else: return True

def makeCircular(num_list):
  result = []
  for idx in range(0, len(num_list)):
    result.append(num_list[idx:]+num_list[0:idx])

  return result

def circularPrimalityTest(num_list, n):
  circular = makeCircular(num_list)

  for c in circular:
    if n == 197: print c
    if not isPrime(to_number(list(c))):
      if n == 197: print c
      return False

  return True


answer = set()


for n in range(2, 1000001):
  if not isPrime(n): continue
  num_list = to_list(n)
  if circularPrimalityTest(num_list, n):
    answer.add(n)
    print n

print answer
print len(answer)
