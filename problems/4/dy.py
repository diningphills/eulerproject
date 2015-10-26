def GetRadixList(n):
	list = []

	if n < 10:	return [n]
	else:
		radix = n % 10
		list = GetRadixList(n/10)
		list.append(radix)
		return list

def isPalindrome(list):
	for i in range(0, len(list)/2):
		if list[i] != list[-(i+1)]:	return False
	return True

biggestPalindrome = 0

for i in range(100, 1000):
	for j in range(i, 1000):
		result = i*j
		if isPalindrome(GetRadixList(result)) and biggestPalindrome < result:
			biggestPalindrome = result

print(biggestPalindrome)