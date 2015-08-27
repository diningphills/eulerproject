def fibonacci(stop):
  a, b = 0, 1
  while a + b <= stop:
    yield a + b
    a, b = b, a + b

def problem():
  gen = fibonacci(4000000)
  return sum(filter(lambda x: x % 2 == 0, gen))

print(problem())