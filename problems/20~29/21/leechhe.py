import math
def d(n):
	limit = int(math.sqrt(n))
	ret = 1
	for i in range(2, limit):
		if n % i == 0 :
			ret += i
			ret += n / i
	if n % limit == 0 :
		ret += limit
	return int(ret)

ans = set()
for i in range(1, 10001):
	temp = d(i)
	if d(temp) == i :
		if temp == i :
			continue
		ans.add(i)
		ans.add(temp)

print (ans)
print (sum(ans))