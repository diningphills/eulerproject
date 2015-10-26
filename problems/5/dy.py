def gcd(*numbers):
	from fractions import gcd
	return reduce(gcd, numbers)

def lcm(*numbers):
	def lcm(a, b):
		return (a*b) // gcd(a, b)
	return reduce(lcm, numbers, 1)

result = 1

for i in range(1,20):
	print("%d*%d/%d = " %(result, i, gcd(result,i))),
	result = (result * i) / gcd(result, i)
	print("%d" %(result))