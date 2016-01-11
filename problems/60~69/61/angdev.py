def assert_eq(expect, actual):
  if expect == actual:
    print('.')
  else:
    print("Expected %s, Actual %s" % (expect, actual))

def sequence(generator, stop):
  i = 1
  while True:
    x = int(generator(i))
    if x > stop:
      return
    yield x
    i += 1

def triangular_numbers(stop):
  return sequence(lambda x: x * (x+1)/2, stop)

def square_numbers(stop):
  return sequence(lambda x: x**2, stop)

def pentagonal_numbers(stop):
  return sequence(lambda x: x*(3*x-1)/2, stop)

def hexagonal_numbers(stop):
  return sequence(lambda x: x*(2*x-1), stop)

def heptagonal_numbers(stop):
  return sequence(lambda x: x*(5*x-3)/2, stop)

def octagonal_numbers(stop):
  return sequence(lambda x: x*(3*x-2), stop)

def tail_cycle_candidates(previous, numbers):
  end_digits = str(previous)[-2:]
  return filter(lambda x: str(x)[0:2] == end_digits, numbers)

def search_cycle(cycle, numbers, *keys):
  if len(keys) == 0:
    return cycle

  current = cycle[-1]
  for key in keys:
    candidates = tail_cycle_candidates(current, numbers[key])
    for c in candidates:
      new_cycle = cycle[:]
      new_cycle.append(c)
      new_keys = set(keys) - set([key])

      result = search_cycle(new_cycle, numbers, *new_keys)
      if result != None and str(result[0])[0:2] == str(result[-1])[-2:]:
        return result

  return None


def problem():
  numbers = {
    'triangular': list(filter(lambda x: x >= 1000, triangular_numbers(10000))),
    'square': list(filter(lambda x: x >= 1000, square_numbers(10000))),
    'pentagonal': list(filter(lambda x: x >= 1000, pentagonal_numbers(10000))),
    'hexagonal': list(filter(lambda x: x >= 1000, hexagonal_numbers(10000))),
    'heptagonal': list(filter(lambda x: x >= 1000, heptagonal_numbers(10000))),
    'octagonal': list(filter(lambda x: x >= 1000, octagonal_numbers(10000))),
  }

  for i in numbers['square']:
    cycle = search_cycle([i], numbers, *(set(numbers.keys()) - set(['square'])))
    if cycle != None:
      return cycle

cycle = problem()
print(cycle)
print(sum(cycle))