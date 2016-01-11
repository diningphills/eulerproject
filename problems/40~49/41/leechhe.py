import math
# n should be 4 or 7.
numbers = [ str(i) for i in range(1,8)]
candidates = []
def dfs(current, i):
	if numbers[i] in current :
		return
	if len(current+numbers[i]) >= 7 :
		candidates.append(current+numbers[i])
		return
	else:
		for j in range(7):
			#print ((current+numbers[i]) + "," + (str(j)))
			dfs(current + numbers[i], j)
			

# 13 15 17 19
for i in range(7):
	dfs('',i)

# exclude even numbers
candidates = list(filter(lambda x: int(x[-1]) % 2 > 0, candidates))
# exclude muptiple of 5
candidates = list(filter(lambda x: x[-1] != '5', candidates))
candidates = [int(i) for i in candidates]
#============================

def isPrime(x):
	limit = math.ceil(x)
	for i in range(11, limit):
		if x % i == 0 :
			return False
	return True;

for number in candidates[::-1]:
	if isPrime(number):
		print (number)
		break
