def assert_eq(expect, actual):
  if expect == actual:
    print('.')
  else:
    print("Expected %s, Actual %s" % (expect, actual))

def shortest_distance(map, width, height):
  shortest_cache = [[0 for x in range(width)] for x in range(height)]

  shortest_cache[0][0] = map[0][0]

  for i in range(1, width):
    shortest_cache[0][i] = shortest_cache[0][i-1] + map[0][i]

  for i in range(1, height):
    shortest_cache[i][0] = shortest_cache[i-1][0] + map[i][0]

  for i in range(1, height):
    for j in range(1, width):
      shortest_cache[i][j] = min(shortest_cache[i-1][j], shortest_cache[i][j-1]) + map[i][j]

  return shortest_cache[height - 1][width - 1]

def problem():
  map = []
  with open('matrix.txt') as f:
    lines = f.readlines()
    for line in lines:
      nums = line.split(',')
      map.append([int(x) for x in nums])
    return shortest_distance(map, 80, 80)

assert_eq(2427, shortest_distance([
  [131, 673, 234, 103, 18],
  [201, 96, 342, 965, 150],
  [630, 803, 746, 422, 111],
  [537, 699, 497, 121, 956],
  [805, 732, 524, 37, 331]
], 5, 5))

print(problem())