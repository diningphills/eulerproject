def assert_eq(expect, actual):
  if expect == actual:
    print('.')
  else:
    print("Expected %s, Actual %s" % (expect, actual))

def is_arithmetic_seq(numbers):
  return len(numbers) == 0 or all(numbers[0] == number for number in numbers)

def seq(generator, count):
  return [generator(n) for n in range(1, count + 1)]

def diff_seq(numbers):
  list = []
  for i in range(len(numbers) - 1):
    list.append(numbers[i + 1] - numbers[i])
  return list

def guess_next_term(numbers):
  if is_arithmetic_seq(numbers):
    return numbers[0]

  diff = diff_seq(numbers)
  return numbers[-1] + guess_next_term(diff)

def sum_bops(generator, degree):
  term_count = degree + 1
  sequence = seq(generator, term_count)
  bop_list = []

  for i in range(1, term_count):
    known_terms = sequence[0:i]
    correct_term = sequence[i]
    guess_term = guess_next_term(known_terms)

    if guess_term != correct_term:
      bop_list.append(guess_term)

  return sum(bop_list)

def example():
  generator = lambda x: x**3
  return sum_bops(generator, 3)

def problem():
  generator = lambda x: 1 - x + x**2 - x**3 + x**4 - x**5 + x**6 - x**7 + x**8 - x**9 + x**10
  return sum_bops(generator, 10)

assert_eq(True, is_arithmetic_seq([1, 1, 1, 1]))
assert_eq([1, 8, 27, 64], seq(lambda x: x**3, 4))
assert_eq([7, 7], diff_seq([1, 8, 15]))

assert_eq(1, guess_next_term([1]))
assert_eq(15, guess_next_term([1, 8]))
assert_eq(58, guess_next_term([1, 8, 27]))

assert_eq(74, example())

print(problem())