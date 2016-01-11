matrix = []
f = open('matrix.txt','r')
for line in f:
	matrix.append([int(i) for i in line.replace('\n','').split(',')])
dp = [[0 for i in range(80)] for j in range(80)]

def GetDP(x, y):
	ret = matrix[x][y]
	if x == 0 and y == 0 : 
		return ret
	if x - 1 < 0 : 
		return ret + dp[x][y-1]
	if y - 1 < 0 :
		return ret + dp[x-1][y]
	return ret + min(dp[x-1][y], dp[x][y-1])

dp[0][0] = matrix[0][0]
for i in range(80):
	for j in range(80):
		dp[i][j] = GetDP(i, j)

print (dp)