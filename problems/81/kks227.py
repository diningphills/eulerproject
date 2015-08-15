max = 80
map = [[0 for x in range(max)] for x in range(max)]
cache = [[0 for x in range(max)] for x in range(max)]

def minCost(r, c):
	global max
	global map
	global cache
	if cache[r][c] >= 0:
		return cache[r][c]
	cache[r][c] = map[r][c]
	if r==max-1 and c==max-1:
		return cache[r][c]
	if r==max-1:
		cache[r][c] += minCost(r, c+1)
		return cache[r][c]
	if c==max-1:
		cache[r][c] += minCost(r+1, c)
		return cache[r][c]
	cache[r][c] += min(minCost(r+1, c), minCost(r, c+1))
	return cache[r][c]

for i in range(max):
	for j in range(max):
		cache[i][j] = -1

f = open('matrix.txt', 'rt')
i = 0
for line in f:
	arr = line.rstrip('\n').split(',')
	j = 0
	for val in arr:
		map[i][j] = int(val)
		j += 1
	i += 1

print(minCost(0, 0))