def word_value(word):
  return sum(map(lambda c: ord(c) - ord('A') + 1, word))

def triangular_number(stop):
  n = 1
  while True:
    t = int(n * (n + 1) / 2)
    if t > stop:
      return
    yield t
    n += 1

def problem():
  with open('words.txt') as f:
    words = eval("[%s]" % f.read())

    upper_bound = 26 * len(max(words, key = lambda x: len(x)))
    triangular_numbers = list(triangular_number(upper_bound))

    triangular_words = filter(lambda x: word_value(x) in triangular_numbers, words)
    return len(triangular_words)

print(problem())