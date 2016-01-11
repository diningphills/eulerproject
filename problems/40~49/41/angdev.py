from itertools import permutations

def is_prime(n):
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

def pandigitals(digit):
  perms = permutations(range(1, digit + 1), digit)
  for tup in perms:
    yield int(''.join(str(x) for x in tup))

def largest_pandigital_prime(digit):
  candidates = list(pandigitals(digit))
  for x in reversed(candidates):
    if is_prime(x):
      return x

  return 0

print(max([largest_pandigital_prime(x) for x in range(1, 10)]))