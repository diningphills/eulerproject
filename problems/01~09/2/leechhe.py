num = [1,1]

def fib(n):
	result = 0
	if n <= 1 :
		return num[n]  
	for i in range(2,n+1) :
		num.append(num[i-1]+num[i-2])
		if num[-1] % 2 == 0 :
			result += num[-1]
		if num[-1] > 4000000 :
			break 
	return result

print (fib(80))
