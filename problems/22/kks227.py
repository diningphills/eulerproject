f = open('names.txt', 'rt')
names = f.readlines()[0].replace('"', '').split(',')
names.sort()
result = 0
for i in range(len(names)):
	for c in names[i]:
		result += (ord(c)-ord('A')+1)*(i+1)
print(result)