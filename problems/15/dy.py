def factorial(n):
	if n==1: return 1
	else:	return n*factorial(n-1)

def path(n, m):
	return factorial(n+m) / (factorial(n)*factorial(m))

print(path(20, 20))