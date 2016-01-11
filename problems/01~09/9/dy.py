def find():	
	for i in range(1, 1001):
		for j in range(i, 1001):
			k = i**2 + j**2
			k = k**0.5
			if (i+j+k) == 1000:	return [i, j, k]

list = find()
result = 1
for element in list:
	result = result*element

print(result)