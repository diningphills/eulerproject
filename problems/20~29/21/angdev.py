def assert_eq(expected, actual):
  if expected == actual:
    print(".")
  else:
    print("Expected %s, but %s" % (expected, actual))

def divisors(n):
  i = 1
  while i <= n/2:
    if n % i == 0:
      yield i
    i += 1

def divisor_sum(n):
  return sum(divisors(n))

def is_amicable_number(n):
  candidate = divisor_sum(n)
  # Exclude perfect numbers
  return candidate != n and divisor_sum(candidate) == n

def amicable_numbers(stop):
  i = 1
  while i < stop:
    if is_amicable_number(i):
      yield i
    i += 1

assert_eq(284, divisor_sum(220))
assert_eq(220, divisor_sum(284))
assert_eq(True, is_amicable_number(220))
assert_eq(False, is_amicable_number(6))

print(sum(amicable_numbers(10001)))