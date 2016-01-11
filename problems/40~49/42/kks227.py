f = open('words.txt', 'rt')
words = f.readlines()[0].replace('"', '').split(',')
tri = [int(i*(i+1)/2) for i in range(50)]
count = 0
for w in words:
	temp = 0
	for c in w:
		temp += ord(c)-ord('A')+1
	if temp in tri:
		count += 1
print(count)