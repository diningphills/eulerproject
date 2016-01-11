def alphabet_map(str):
  return map(lambda c: ord(c) - ord('A') + 1, str)

def problem():
  with open('names.txt') as f:
    names = eval("[%s]" % f.read())
    names = sorted(names)

    scores = []
    for index, name in enumerate(names):
      score = sum(alphabet_map(name)) * (index + 1)
      scores.append(score)

    return sum(scores)

print(problem())