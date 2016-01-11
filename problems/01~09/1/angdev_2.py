def assert_eq(expected, actual):
  if expected == actual:
    print(".")
  else:
    print("Expected %s, but %s" % (expected, actual))

def fizzbuzz(stop):
  i = 1
  while i < stop:
    if i % 3 == 0 or i % 5 == 0:
      yield i
    i += 1

print(sum(fizzbuzz(1000)))

assert_eq(23, sum(fizzbuzz(10)))