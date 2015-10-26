def GetRadixList(n):
	list = []

	if n < 10:	return [n]
	else:
		radix = n % 10
		list = GetRadixList(n/10)
		list.append(radix)
		return list

list = GetRadixList(2**1000)
sum = 0
for element in list:
	sum += element

print(sum)