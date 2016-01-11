
sum = 0

a0 = 1
a1 = 2

sum += a1

while True:
	a2 = a0 + a1
	if a2 > 4000000:	break
	if a2 % 2 == 0:
		sum += a2
	a0 = a1
	a1 = a2

print(sum)