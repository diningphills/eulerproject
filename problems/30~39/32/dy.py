answer = set()

# permutation
def permutations(iterable, r=None):
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = range(n)
  cycles = range(n, n-r, -1)
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return

# 39 * 186 = 7254
# a * b = c?
def test_equality(a, b, c):
  return a*b == c

# test pendigital
def test_pendigital(left_side, right_side):
  c = to_number(right_side)

  for idx in range(1, len(left_side)):
    a = to_number(left_side[0:idx])
    b = to_number(left_side[idx:])
    if a*b == c:
      answer.add(c)
      return True

  return False

# list to number
def to_number(n_list):
  final_number = 0
  for (idx, num) in enumerate(n_list):
    rdx = len(n_list) - idx - 1
    final_number = final_number + (num * 10**rdx)
  return final_number


target = set([1,2,3,4,5,6,7,8,9])

possible_right = permutations(target, 4)
for right in possible_right:
  possible_left = permutations(target-set(right), 5)
  for left in possible_left:
    if test_pendigital(list(left), list(right)): break

print sum(answer)
