f = open("words.txt", "r")
def triangle(n):
	return int(n * (n+1) / 2)
def word_value(word):
	return sum(map(lambda char: ord(char), word)) - len(word) * (ord('A') -1)

triangle_numbers = [triangle(i) for i in range(1,100)]
print (triangle_numbers)

count = 0
for line in f:
	for word in line.split(","):
		if word_value(word[1:-1]) in triangle_numbers :
			count += 1

print (count)