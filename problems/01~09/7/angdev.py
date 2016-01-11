def assert_eq(expect, actual):
  if expect == actual:
    print('.')
  else:
    print("Expected %s, Actual %s" % (expect, actual))

def prime_number(index):
  primes = [2]
  current = primes[-1]

  while len(primes) < index:
    is_prime = True
    current += 1
    for p in primes:
      if current < p * p:
        break
      if current % p == 0:
        is_prime = False
        break

    if is_prime:
      primes.append(current)

  return primes[index - 1]

print(prime_number(10001))

assert_eq(2, prime_number(1))
assert_eq(3, prime_number(2))
assert_eq(5, prime_number(3))