fibo = [1, 2]
while fibo[-1]<=4000000:
	fibo.append(fibo[-1]+fibo[-2])
print (sum( filter(lambda n: n%2==0, fibo) ))