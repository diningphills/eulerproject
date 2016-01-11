def assert_eq(expected, actual):
  if expected == actual:
    print(".")
  else:
    print("Expected %s, but %s" % (expected, actual))

def is_fizzbuzz(x):
  return x % 3 == 0 or x % 5 == 0

def fizzbuzz_sum(start, stop):
  fizzbuzz = [x for x in range(start, stop) if is_fizzbuzz(x)]
  return sum(fizzbuzz)

print(fizzbuzz_sum(1, 1000))

assert_eq(23, fizzbuzz_sum(1, 10))